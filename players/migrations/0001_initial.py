# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField()),
                ('pos', models.CharField(choices=[('', ''), ('S', '舉球'), ('WS', '大砲/攻擊手'), ('MB', '攔中'), ('O', '輔舉'), ('L', '自由')], default=('', ''), max_length=2)),
                ('mg_pos', models.CharField(choices=[('player', '球員'), ('leader', '隊長'), ('vice leader', '副隊長'), ('financial', '總務'), ('manager_m', '男排球經'), ('manager_w', '女排球經')], default=('player', '球員'), max_length=20)),
                ('photo', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
