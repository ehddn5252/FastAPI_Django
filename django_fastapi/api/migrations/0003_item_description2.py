# Generated by Django 2.2.1 on 2021-11-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description2',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]