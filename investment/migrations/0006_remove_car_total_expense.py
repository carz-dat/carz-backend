# Generated by Django 4.2.1 on 2023-05-09 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0005_alter_car_year_made'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='total_expense',
        ),
    ]
