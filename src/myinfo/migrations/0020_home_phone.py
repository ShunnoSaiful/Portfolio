# Generated by Django 3.1.3 on 2020-11-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0019_remove_home_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='phone',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
