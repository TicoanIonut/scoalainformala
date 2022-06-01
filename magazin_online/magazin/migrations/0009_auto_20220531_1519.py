# Generated by Django 3.2.5 on 2022-05-31 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazin', '0008_remove_produs_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresacomanda',
            name='adresa',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='adresacomanda',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazin.client'),
        ),
        migrations.AlterField(
            model_name='adresacomanda',
            name='cod_postal',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='adresacomanda',
            name='comanda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazin.comanda'),
        ),
        migrations.AlterField(
            model_name='adresacomanda',
            name='judet',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='adresacomanda',
            name='oras',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='utilizator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='id_tranzactie',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='comandaprodus',
            name='cantitate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comandaprodus',
            name='comanda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazin.comanda'),
        ),
        migrations.AlterField(
            model_name='comandaprodus',
            name='produs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazin.produs'),
        ),
        migrations.AlterField(
            model_name='produs',
            name='price',
            field=models.FloatField(default=10.55),
        ),
    ]
