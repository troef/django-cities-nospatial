# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlternativeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('language', models.CharField(max_length=100)),
                ('is_preferred', models.BooleanField(default=False)),
                ('is_short', models.BooleanField(default=False)),
                ('is_colloquial', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name=b'ascii name')),
                ('slug', models.CharField(max_length=200)),
                ('name_std', models.CharField(db_index=True, max_length=200, verbose_name=b'standard name')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('population', models.IntegerField()),
                ('elevation', models.IntegerField(null=True)),
                ('kind', models.CharField(max_length=10)),
                ('timezone', models.CharField(max_length=40)),
                ('alt_names', models.ManyToManyField(to='cities.AlternativeName')),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name=b'ascii name')),
                ('slug', models.CharField(max_length=200)),
                ('code', models.CharField(db_index=True, max_length=2)),
                ('code3', models.CharField(db_index=True, max_length=3)),
                ('population', models.IntegerField()),
                ('area', models.IntegerField(null=True)),
                ('currency', models.CharField(max_length=3, null=True)),
                ('currency_name', models.CharField(max_length=50, null=True)),
                ('languages', models.CharField(max_length=250, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('continent', models.CharField(max_length=2)),
                ('tld', models.CharField(max_length=5)),
                ('capital', models.CharField(max_length=100)),
                ('alt_names', models.ManyToManyField(to='cities.AlternativeName')),
                ('neighbours', models.ManyToManyField(related_name='_country_neighbours_+', to='cities.Country')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name=b'ascii name')),
                ('slug', models.CharField(max_length=200)),
                ('name_std', models.CharField(db_index=True, max_length=200, verbose_name=b'standard name')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('population', models.IntegerField()),
                ('alt_names', models.ManyToManyField(to='cities.AlternativeName')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name=b'ascii name')),
                ('slug', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('region_name', models.CharField(db_index=True, max_length=100)),
                ('subregion_name', models.CharField(db_index=True, max_length=100)),
                ('district_name', models.CharField(db_index=True, max_length=100)),
                ('alt_names', models.ManyToManyField(to='cities.AlternativeName')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postal_codes', to='cities.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name=b'ascii name')),
                ('slug', models.CharField(max_length=200)),
                ('name_std', models.CharField(db_index=True, max_length=200, verbose_name=b'standard name')),
                ('code', models.CharField(db_index=True, max_length=200)),
                ('alt_names', models.ManyToManyField(to='cities.AlternativeName')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subregion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name=b'ascii name')),
                ('slug', models.CharField(max_length=200)),
                ('name_std', models.CharField(db_index=True, max_length=200, verbose_name=b'standard name')),
                ('code', models.CharField(db_index=True, max_length=200)),
                ('alt_names', models.ManyToManyField(to='cities.AlternativeName')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.Region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.Region'),
        ),
        migrations.AddField(
            model_name='city',
            name='subregion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.Subregion'),
        ),
    ]
