# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('invoice_id', models.CharField(max_length=255, verbose_name='invoice_id')),
                ('receipt_number', models.CharField(max_length=255, verbose_name='receipt_number')),
                ('order_id', models.CharField(max_length=255, verbose_name='order_id')),
                ('status', models.CharField(max_length=255, verbose_name='status')),
                ('payment_id', models.CharField(null=True, max_length=255, verbose_name='invoice_id')),
                ('expire_by', models.CharField(null=True, max_length=255, verbose_name='expire_by')),
                ('issued_at', models.CharField(max_length=255, verbose_name='issued_at')),
                ('paid_at', models.CharField(null=True, max_length=255, verbose_name='paid_at')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('currency', models.CharField(max_length=255, verbose_name='currency')),
                ('short_url', models.CharField(max_length=255, verbose_name='short_url')),
                ('conference', models.PositiveIntegerField(default=0, verbose_name='conference')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('order_id', models.CharField(max_length=255, verbose_name='order_id')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('currency', models.CharField(null=True, max_length=255, verbose_name='currency')),
                ('status', models.CharField(null=True, max_length=255, verbose_name='status')),
                ('created_at', models.CharField(null=True, max_length=255, verbose_name='created_at')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('payment_id', models.CharField(max_length=255, verbose_name='payment_id')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('currency', models.CharField(null=True, max_length=255, verbose_name='currency')),
                ('status', models.CharField(null=True, max_length=255, verbose_name='status')),
                ('order_id', models.CharField(null=True, max_length=255, verbose_name='order_id')),
                ('invoice_id', models.CharField(null=True, max_length=255, verbose_name='invoice_id')),
                ('international', models.BooleanField(default=False, db_index=True, verbose_name='international?')),
                ('amount_refunded', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('refund_status', models.CharField(null=True, max_length=255, verbose_name='refund_status')),
                ('email', models.CharField(null=True, max_length=255, verbose_name='email')),
                ('contact', models.CharField(null=True, blank=True, max_length=15, verbose_name='contact')),
                ('fee', models.PositiveIntegerField(default=0, verbose_name='fee')),
                ('service_tax', models.PositiveIntegerField(default=0, verbose_name='service_tax')),
                ('created_at', models.CharField(null=True, max_length=255, verbose_name='created_at')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RazorpayKeys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('api_key', models.CharField(max_length=255, verbose_name='api key')),
                ('api_secret', models.CharField(max_length=255, verbose_name='api secret')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
