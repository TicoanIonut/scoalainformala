# Generated by Django 3.2.5 on 2022-05-13 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_comenzii', models.DateTimeField(auto_now_add=True)),
                ('complet', models.BooleanField(default=False, null=True)),
                ('id_tranzactie', models.CharField(max_length=200, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazin.client')),
            ],
        ),
        migrations.CreateModel(
            name='Produs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComandaProdus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantitate', models.IntegerField(blank=True, default=0, null=True)),
                ('data_adaugarii', models.DateTimeField(auto_now_add=True)),
                ('comanda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazin.comanda')),
                ('produs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazin.produs')),
            ],
        ),
        migrations.CreateModel(
            name='AdresaComanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresa', models.CharField(max_length=200, null=True)),
                ('oras', models.CharField(max_length=200, null=True)),
                ('judet', models.CharField(max_length=200, null=True)),
                ('cod_postal', models.CharField(max_length=200, null=True)),
                ('data_adaugarii', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazin.client')),
                ('comanda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazin.comanda')),
            ],
        ),
    ]
