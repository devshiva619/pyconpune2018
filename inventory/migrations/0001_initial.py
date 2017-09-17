# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_conference', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('gender', models.CharField(max_length=255, verbose_name='gender')),
                ('size', models.CharField(max_length=5, verbose_name='size')),
                ('limit', models.PositiveIntegerField(default=0, verbose_name='limit')),
                ('price', models.PositiveIntegerField(default=0, db_index=True, verbose_name='price')),
                ('description', models.CharField(null=True, max_length=255, verbose_name='description')),
                ('image_base64_title', models.CharField(null=True, max_length=255, blank=True, verbose_name='image title')),
                ('image_base64_text', models.TextField(null=True, blank=True, verbose_name='image url')),
                ('is_limit_reached', models.BooleanField(default=False, db_index=True, verbose_name='limit reached?')),
                ('disabled', models.BooleanField(default=False, db_index=True, verbose_name='disabled?')),
                ('conference', models.ForeignKey(to='symposion_conference.Conference', verbose_name='conference')),
            ],
            options={
                'verbose_name_plural': 'tshirts',
                'verbose_name': 'tshirt',
            },
        ),
        migrations.CreateModel(
            name='UserTshirt',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('invoice', models.CharField(default=0, max_length=255, verbose_name='invoice')),
                ('tshirt', models.ForeignKey(to='inventory.Tshirt')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user tshirts',
                'ordering': ['-timestamp'],
                'verbose_name': 'user tshirt',
            },
        ),
    ]
