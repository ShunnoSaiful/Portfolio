# Generated by Django 3.1.3 on 2020-11-14 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0015_auto_20201114_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recentportfolio',
            old_name='tag',
            new_name='rptag',
        ),
    ]