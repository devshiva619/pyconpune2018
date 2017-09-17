# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_conference', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuxiliaryTicket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('title', models.CharField(verbose_name='name', max_length=255)),
                ('limit', models.PositiveIntegerField(verbose_name='limit', default=0)),
                ('price', models.PositiveIntegerField(verbose_name='price', default=0)),
                ('description', models.CharField(verbose_name='description', null=True, max_length=255)),
                ('image_base64_title', models.CharField(verbose_name='image title', null=True, blank=True, max_length=255)),
                ('image_base64_text', models.TextField(null=True, blank=True, verbose_name='image url')),
                ('is_limit_reached', models.BooleanField(verbose_name='limit reached?', default=False, db_index=True)),
                ('disabled', models.BooleanField(verbose_name='disabled?', default=False, db_index=True)),
                ('conference', models.ForeignKey(verbose_name='conference', to='symposion_conference.Conference')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('code', models.CharField(verbose_name='coupon', max_length=20)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('title', models.CharField(verbose_name='name', max_length=255)),
                ('limit', models.PositiveIntegerField(verbose_name='limit', default=0)),
                ('price', models.PositiveIntegerField(verbose_name='price', default=0, db_index=True)),
                ('description', models.CharField(verbose_name='description', null=True, max_length=255)),
                ('image_base64_title', models.CharField(verbose_name='image title', null=True, blank=True, max_length=255)),
                ('image_base64_text', models.TextField(null=True, blank=True, verbose_name='image url')),
                ('is_limit_reached', models.BooleanField(verbose_name='limit reached?', default=False, db_index=True)),
                ('disabled', models.BooleanField(verbose_name='disabled?', default=False, db_index=True)),
                ('conference', models.ForeignKey(verbose_name='conference', to='symposion_conference.Conference')),
            ],
            options={
                'verbose_name_plural': 'tickets',
                'verbose_name': 'ticket',
            },
        ),
        migrations.CreateModel(
            name='TicketAddons',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('title', models.CharField(verbose_name='name', max_length=255)),
                ('price', models.PositiveIntegerField(verbose_name='price', default=0)),
                ('ticket', models.ForeignKey(to='ticket.Ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserTicket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('uuid', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('invoice', models.CharField(verbose_name='invoice', max_length=255, default=0)),
                ('auxiliary_ticket_id', models.CommaSeparatedIntegerField(verbose_name='auxiliary ticket', max_length=200, default=0)),
                ('is_payment_done', models.BooleanField(verbose_name='payment done?', default=False)),
                ('ticket', models.ForeignKey(to='ticket.Ticket')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user tickets',
                'ordering': ['-timestamp'],
                'verbose_name': 'user ticket',
            },
        ),
    ]
