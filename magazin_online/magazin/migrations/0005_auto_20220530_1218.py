# Generated by Django 3.2.5 on 2022-05-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0004_remove_produs_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='produs',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='complet',
            field=models.BooleanField(default=False),
        ),
    ]