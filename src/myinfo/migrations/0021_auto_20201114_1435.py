# Generated by Django 3.1.3 on 2020-11-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0020_home_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='phone',
        ),
        migrations.AddField(
            model_name='home',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
