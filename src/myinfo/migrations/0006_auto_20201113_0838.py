# Generated by Django 3.1.3 on 2020-11-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0005_auto_20201113_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='contact_no',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]