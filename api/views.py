# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


class VendorViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]

    def list(self, request):
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = VendorSerializer(data=request.data)
        # print(request.data["name"])
        # return Response(status=200)
        data = request.data

        if serializer.is_valid():
            serializer.save()

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        vendordata = {
            "name": data["name"],
            "vendor": serializer.data["id"]

        }
        vendorserializer = HistoricalPerformanceSerializer(data=vendordata)
        if (vendorserializer.is_valid()):
            vendorserializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(vendorserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Vendor.objects.all()
        vendor = get_object_or_404(queryset, pk=pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def update(self, request, pk=None):
        vendor = Vendor.objects.get(pk=pk)
        vendor1 = VendorSerializer(vendor)
        data = request.data
        keys = data.keys

        for key in keys:
            vendor1[key] = data[key]
        print(vendor1)
        serializer = VendorSerializer(vendor, data=vendor1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        vendor = Vendor.objects.get(pk=pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'], url_path='performance')
    def performance(self, request, pk=None, **kwargs):
        # vebdor_id = kwargs.get('vendorid')
        vendor = Vendor.objects.get(pk=pk)
        performances = HistoricalPerformance.objects.filter(vendor=vendor)
        serializer = HistoricalPerformanceSerializer(performances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchaseOrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        vendor_id = request.query_params.get('vendor', None)
        queryset = PurchaseOrder.objects.all()
        if vendor_id:
            queryset = queryset.filter(vendor_reference=vendor_id)
        serializer = PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = PurchaseOrder.objects.all()
        purchase_order = get_object_or_404(queryset, pk=pk)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        purchase_order1 = PurchaseOrderSerializer(purchase_order)
        purchase_order1 = purchase_order1.data

        if "status" in request.data:
            all_po = PurchaseOrder.objects.filter(
                vendor=purchase_order.vendor)
            po_with_qr = PurchaseOrder.objects.filter(
                vendor=purchase_order.vendor).exclude(quality_rating=None)
            sum_of_quality_rating = 0

            for i in po_with_qr:
                sum_of_quality_rating += i.quality_rating
         

            total_no_of_objects = len(all_po)
            all_completed_po = all_po.filter(status="Completed")
            total_completed_po = len(all_completed_po)
            performance = HistoricalPerformance.objects.get(
                vendor=purchase_order.vendor)

            performance_serializer = HistoricalPerformanceSerializer(
                performance)
            on_time_delivery_rate = performance.on_time_delivery_rate
            performance_serializer = performance_serializer.data
            if ("quality_rating" in request.data):
                sum_of_quality_rating += request.data["quality_rating"]
                performance_serializer["quality_rating"] = sum_of_quality_rating/len(
                    po_with_qr+1)
            else:
                performance_serializer["quality_rating"] = sum_of_quality_rating/len(
                    po_with_qr)

            if (request.data["status"] == "Cancelled"):
                performance_serializer["fulfillment_rate"] = (
                    total_completed_po)/total_no_of_objects

            if (request.data["status"] == "Completed"):
                performance_serializer["fulfillment_rate"] = (total_completed_po+1) / \
                    total_no_of_objects

            
                sum_of_all_timed_po = on_time_delivery_rate*total_completed_po
                if (timezone.now() <= purchase_order.delivery_date):
                    sum_of_all_timed_po += 1
                    total_completed_po += 1
                    on_time_delivery_rate = sum_of_all_timed_po/total_completed_po
              
                else:
                    on_time_delivery_rate = sum_of_all_timed_po / \
                        (total_completed_po+1)

                performance_serializer.on_time_delivery_rate = on_time_delivery_rate
                performance_serializer = HistoricalPerformanceSerializer(
                    performance, data=performance_serializer)
                if performance_serializer.is_valid():
                    performance_serializer.save()
                else:
                    return Response(performance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for key in request.data:
            print(key)
            purchase_order1[key] = request.data[key]

        serializer = PurchaseOrderSerializer(
            purchase_order, data=purchase_order1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def performance(self, request, pk=None,):

        purchase_order = PurchaseOrder.objects.get(pk=pk)
        count = PurchaseOrder.objects.filter(
            vendor=purchase_order.vendor).exclude(acknowledgment_date__isnull=True).count()
        acktime = HistoricalPerformance.objects.get(
            vendor=purchase_order.vendor)
        sum = acktime.average_response_time*count
        response_time = timezone.now() - purchase_order.issue_date
        response_time = response_time.total_seconds()/3600
        response_time = (response_time+sum)/(count+1)
        return Response(status=200)
    



