# Generated by Django 3.0.3 on 2020-02-21 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='item_image',
        ),
    ]