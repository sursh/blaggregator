# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-13 14:26


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161201_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted_or_crawled']},
        ),
    ]
