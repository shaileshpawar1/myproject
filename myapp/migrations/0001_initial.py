# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_C1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('email', models.EmailField(verbose_name='email', max_length=60, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('email', models.EmailField(verbose_name='email', max_length=60, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.CharField(verbose_name='USER', max_length=50)),
                ('Created_at', models.DateTimeField(verbose_name='Cdate', auto_now_add=True)),
                ('Updated_at', models.DateTimeField(verbose_name='Udate', auto_now=True)),
            ],
            options={
                'db_table': 'Post',
            },
        ),
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rno', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='user1',
            field=models.ForeignKey(to='myapp.User1'),
        ),
    ]
