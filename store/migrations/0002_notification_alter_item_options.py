# Generated by Django 4.2.6 on 2024-01-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('read', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
    ]
