# Generated by Django 4.0.4 on 2022-07-25 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_rename_donationtype_tbl_donation_itemname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_donation',
            name='itemname',
        ),
    ]
