# Generated by Django 3.1.3 on 2020-11-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0021_auto_20201114_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='phone_no',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
