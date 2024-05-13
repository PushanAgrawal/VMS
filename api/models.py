from django.db import models
from django.utils import timezone
from enum import Enum
# from  phonenumber_field.modelfields import PhoneNumberField


# This model stores essential information about each vendor and their performance metrics.
class Vendor(models.Model):

    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    # on_time_delivery_rate = models.FloatField(default=0)
    # quality_rating_avg = models.FloatField(default=0)
    # average_response_time = models.FloatField(default=0)
    # fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):

    class statusChoices(models.TextChoices):
        Completed = 'Completed'
        Pending = 'Pending'
        Canceled = 'Canceled'

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(
    max_length=50, choices=statusChoices, default=statusChoices.Pending)
    quality_rating = models.FloatField(blank=True, null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.po_number


class HistoricalPerformance(models.Model):

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return f"{self.vendor} - {self.date}"
