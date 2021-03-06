# Generated by Django 2.0.6 on 2018-06-12 07:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0004_auto_20180611_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team2', models.CharField(max_length=100)),
                ('dtime', models.DateTimeField(default=datetime.datetime.now)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fifa.Match')),
            ],
        ),
    ]
