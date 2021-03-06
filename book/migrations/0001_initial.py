# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-12 03:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('translator', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('introduction', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_user', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='update_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
