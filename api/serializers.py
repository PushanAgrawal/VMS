from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ('username', 'email')


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'


# class HistoricalPerformanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HistoricalPerformance
#         fields = ['on_time_delivery_rate', 'quality_rating_avg',
#                   'average_response_time', 'fulfillment_rate']
