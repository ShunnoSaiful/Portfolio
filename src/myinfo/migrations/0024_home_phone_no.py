# Generated by Django 3.1.3 on 2020-11-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0023_remove_home_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='phone_no',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
