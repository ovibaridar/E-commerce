# Generated by Django 4.2.3 on 2023-07-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_hading', models.CharField(max_length=100)),
                ('blog_image', models.CharField(max_length=100)),
            ],
        ),
    ]
