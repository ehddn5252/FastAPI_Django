# Generated by Django 3.2.9 on 2021-11-18 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Login', to='auth.user'),
            preserve_default=False,
        ),
    ]
