# Generated by Django 4.2.1 on 2023-05-09 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('GEL', 'GEL')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='total_expense',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='auction_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='shipment_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='ExpensesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('PRT', 'Parts'), ('LBR', 'Labor')], max_length=255)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('GEL', 'GEL')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='investment.car')),
            ],
        ),
    ]