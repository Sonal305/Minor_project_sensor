# Generated by Django 3.1.4 on 2020-12-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_auto_20201202_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPSP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='sensor',
            name='area',
            field=models.CharField(choices=[('KIT', 'Kitchen'), ('HAL', 'Hall'), ('GAR', 'Garden'), ('BAT', 'Bathroom')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='type',
            field=models.CharField(choices=[('FIRE', 'Fire'), ('GAS', 'Gas Leakage'), ('WAT', 'Water Leakage'), ('BURG', 'Burglary')], max_length=4),
        ),
    ]