# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-11 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('as2', '0008_messagerecieved'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessageRecieved',
        ),
    ]