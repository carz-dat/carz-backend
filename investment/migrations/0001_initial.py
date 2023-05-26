# Generated by Django 4.2.1 on 2023-05-09 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('engine_type', models.CharField(blank=True, max_length=255, null=True)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.make')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_made', models.DateField(blank=True, null=True)),
                ('date_of_purchase', models.DateField(blank=True, null=True)),
                ('date_of_sell', models.DateField(blank=True, null=True)),
                ('shipment_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auction_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='cars/')),
                ('car_url', models.URLField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.carmodel')),
            ],
        ),
    ]