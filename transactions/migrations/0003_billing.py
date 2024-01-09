# Generated by Django 4.2.6 on 2023-12-28 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_sale_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.sale')),
            ],
        ),
    ]
