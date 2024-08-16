# Generated by Django 5.0.7 on 2024-08-16 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintBilling',
            fields=[
                ('billing_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=225)),
                ('quantity', models.ImageField(upload_to='')),
                ('rate', models.FloatField()),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.complaint')),
            ],
            options={
                'db_table': 'complaint_bill',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('receipt_id', models.AutoField(primary_key=True, serialize=False)),
                ('receipt_date', models.DateField()),
                ('payment_type', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Online', 'Online'), ('Not Paid', 'Not Paid')], max_length=50)),
                ('receipt_amount', models.FloatField()),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.complaint')),
            ],
            options={
                'db_table': 'receipt',
            },
        ),
    ]
