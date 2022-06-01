# Generated by Django 3.2.5 on 2022-05-30 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazin', '0005_auto_20220530_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='utilizator',
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='produs',
            name='imagine',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
