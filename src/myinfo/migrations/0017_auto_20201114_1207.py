# Generated by Django 3.1.3 on 2020-11-14 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0016_auto_20201114_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreviews',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
