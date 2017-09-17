# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('groups', models.ManyToManyField(to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', verbose_name='groups', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', blank=True, help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions', related_query_name='user')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(null=True, blank=True, max_length=255, verbose_name='last name')),
                ('contact', models.CharField(null=True, blank=True, max_length=15, verbose_name='contact')),
                ('location', models.CharField(null=True, blank=True, max_length=255, verbose_name='location')),
                ('age_group', models.CharField(null=True, blank=True, max_length=255, choices=[('1', 'Less than 10'), ('2', '11-17'), ('3', '18-24'), ('4', '25-34'), ('5', '35-44'), ('6', '45 and over')], verbose_name='age group')),
                ('gender', models.CharField(null=True, blank=True, max_length=255, verbose_name='gender')),
                ('occupation', models.CharField(null=True, blank=True, max_length=1, choices=[('W', 'Working Professional'), ('S', 'Student'), ('U', 'Temporarily Unemployed'), ('C', 'Carer'), ('R', 'Retired')], verbose_name='occupation')),
                ('company', models.CharField(null=True, blank=True, max_length=255, verbose_name='company')),
                ('job_title', models.CharField(null=True, blank=True, max_length=255, verbose_name='job title')),
                ('website', models.URLField(null=True, blank=True)),
                ('subscribed', models.BooleanField(default=False, verbose_name='subscribed')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'verbose_name': 'Profile',
            },
        ),
    ]
