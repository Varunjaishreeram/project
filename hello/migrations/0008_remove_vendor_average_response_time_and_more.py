# Generated by Django 5.0 on 2023-12-14 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='average_response_time',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='fulfillment_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='on_time_delivery_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='quality_rating_avg',
        ),
    ]
