# Generated by Django 4.2.6 on 2023-12-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='payment_method',
            field=models.CharField(blank='True', choices=[('VISA', 'VISA'), ('CS', 'CASH'), ('BK', 'BANK')], max_length=20, null=True),
        ),
    ]
