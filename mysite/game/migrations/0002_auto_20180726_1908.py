# Generated by Django 2.0.6 on 2018-07-27 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='challenges_completed',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='name',
        ),
        migrations.AddField(
            model_name='appuser',
            name='level',
            field=models.IntegerField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='appuser',
            name='nickname',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='appuser',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='appuser',
            name='xp',
            field=models.IntegerField(default=0, max_length=200),
        ),
    ]
