# Generated by Django 2.2.1 on 2021-11-17 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_item_description2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description2',
        ),
    ]