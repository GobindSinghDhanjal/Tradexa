# Generated by Django 4.0 on 2021-12-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_weight', models.IntegerField()),
                ('product_price', models.CharField(max_length=10)),
                ('created_at', models.CharField(max_length=50)),
                ('updated_at', models.CharField(max_length=50)),
            ],
        ),
    ]
