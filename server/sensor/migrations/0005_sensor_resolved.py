# Generated by Django 3.1.4 on 2020-12-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0004_auto_20201202_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
