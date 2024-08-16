from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel

class Customer(BaseModel):
    full_name = models.TextField(max_length = 50)
    address = models.TextField(max_length = 100)
    email = models.TextField(max_length = 50)
    phone = models.TextField(max_length = 50)
    password = models.TextField(max_length = 50)
    terms_and_conditions = models.TextField(max_length = 50)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'customer'


class Admin(BaseModel):
    full_name = models.TextField(max_length = 50)
    address = models.TextField(max_length = 100)
    email = models.TextField(max_length = 50)
    phone = models.TextField(max_length = 50)
    password = models.TextField(max_length = 50)
    terms_and_conditions = models.TextField(max_length = 50)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'admin'


class Technician(BaseModel):
    full_name = models.TextField(max_length = 50)
    address = models.TextField(max_length = 100)
    email_id = models.EmailField(unique=True)
    phone = models.TextField(max_length = 50)
    password = models.TextField(max_length = 50)
    terms_and_conditions = models.TextField(max_length = 50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'technician'

