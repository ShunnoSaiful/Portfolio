# Generated by Django 3.1.3 on 2020-11-14 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0022_auto_20201114_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='phone_no',
        ),
    ]
