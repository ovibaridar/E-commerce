# Generated by Django 4.2.3 on 2023-07-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_qrname'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrname',
            name='image_information',
            field=models.CharField(default='', max_length=100),
        ),
    ]
