# Generated by Django 4.1 on 2022-08-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='custormer',
            new_name='customer',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='registration_date',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]