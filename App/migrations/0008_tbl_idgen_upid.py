# Generated by Django 4.0.3 on 2022-06-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_tbl_volunteer_allot_allot_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_idgen',
            name='upid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
