# Generated by Django 4.1.5 on 2023-01-06 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_seller_alter_customer_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customer_tb',
        ),
        migrations.AlterModelTable(
            name='seller',
            table='seller_tb',
        ),
    ]
