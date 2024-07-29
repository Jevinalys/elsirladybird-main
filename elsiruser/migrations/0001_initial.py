# Generated by Django 5.0.3 on 2024-07-15 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('book_date', models.CharField(max_length=50)),
                ('book_time', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=266)),
                ('product_description', models.TextField(null=True)),
                ('units', models.CharField(choices=[(' ', ' '), ('Kg', 'Kilograms'), ('g', 'Grams')], default=' ', max_length=10)),
                ('total_units', models.IntegerField(null=True)),
                ('unit_buying_price', models.IntegerField(null=True)),
                ('unit_selling_price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=266)),
                ('service_description', models.CharField(max_length=266, null=True)),
                ('service_price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('debt', models.IntegerField(blank=True, default=0, null=True)),
                ('loyalty_points', models.IntegerField(blank=True, default=0, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('profile_pic', models.ImageField(blank=True, default='user.png', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, null=True)),
                ('services', models.CharField(default='', max_length=255)),
                ('payment_mode', models.CharField(choices=[('cash', 'cash'), ('Mpesa', 'Mpesa')], default='cash', max_length=10)),
                ('mpesa_code', models.CharField(max_length=255, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=40)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='elsiruser.customer')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
