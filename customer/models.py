from django.db import models
from base.models import BaseModel
from accounts.models import Customer, Technician, Admin

class Complaint(BaseModel):
    CUSTOMER_TYPE_CHOICES = [
        ('type1', 'type1'),
        ('type2', 'type2'),
        ('type3', 'type3'),
        ('type4', 'type4'),
        ('type5', 'type5')
    ]

    COMPLAINT_TYPE_CHOICES = [
        ('choice1', 'choice1'),
        ('choice2', 'choice2'),
        ('choice3', 'choice3'),
        ('choice4', 'choice4'),
        ('choice5', 'choice5'),
    ]

    PAYMENT_STATUS = [
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
        ('Cancelled', 'Cancelled'),
    ]

    TICKET_STATUS = [
        ('Not Registered', 'Not Registered'),
        ('Pending', 'Pending'),
        ('Send to Billing', 'Send to Billing'),
        ('Resolved', 'Resolved'),
    ]

    PAYMENT_TYPE = [
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Online', 'Online'),
        ('Not Paid', 'Not Paid'),
    ]

    complaint_id = models.CharField(max_length = 50)
    complaint_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    customer_type = models.CharField(max_length = 50, choices=CUSTOMER_TYPE_CHOICES)
    complaint_type = models.CharField(max_length = 50, choices=COMPLAINT_TYPE_CHOICES)
    is_resolve = models.BooleanField(default=False)
    technician = models.ForeignKey(Technician, null=True, blank=True, on_delete=models.SET_NULL)
    token = models.DateTimeField(null=True, blank=True)
    token_number = models.CharField(max_length=50, null=True, blank=True)
    machine_type = models.CharField(max_length=100, null=True, blank=True)
    machine_model = models.CharField(max_length=100, null=True, blank=True)
    machine_no = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPE)
    collected_amount = models.CharField(max_length=100, null=True, blank=True)
    ticket_status = models.CharField(max_length=50, choices=TICKET_STATUS)
    





    def __str__(self):
        return self.complaint_id

class SalesOrder(BaseModel):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
    ]

    REFERENCE_CHOICES = [
        ('Amazon', 'Amazon'),
        ('Flipkart', 'Flipkart'),
        ('India Mart', 'India Mart'),
        ('Alibaba', 'Alibaba'),
    ]
    current_date = models.DateField()
    follow_up_date = models.DateField()
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    reference = models.CharField(max_length=255, choices=REFERENCE_CHOICES)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'sales_order' 


class BillingItem(BaseModel):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    sales_executive = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)

    class Meta:
        db_table = 'billing_item'