# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('post', models.CharField(max_length=2048)),
            ],
        ),
    ]