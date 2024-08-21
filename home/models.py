from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

    class Meta:
        db_table = 'contact'
