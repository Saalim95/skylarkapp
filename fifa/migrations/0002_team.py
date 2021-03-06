# Generated by Django 2.0.6 on 2018-06-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('followers', models.ManyToManyField(related_name='_team_followers_+', to='fifa.Country')),
            ],
        ),
    ]
