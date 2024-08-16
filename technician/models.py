from django.db import models
from customer.models import Complaint

class ComplaintBilling(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    billing_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=225)
    quantity = models.ImageField()
    rate = models.FloatField()

    class Meta:
        db_table = 'complaint_bill'


class Receipt(models.Model):
    PAYMENT_TYPE = [
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Online', 'Online'),
        ('Not Paid', 'Not Paid'),
    ]
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    receipt_id = models.AutoField(primary_key=True)
    receipt_date = models.DateField()
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPE)
    receipt_amount = models.FloatField()

    class Meta:
        db_table = 'receipt'





