# Generated by Django 5.0.7 on 2024-09-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elsiruser', '0004_alter_customer_loyalty_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales_Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=266)),
                ('servicePrice', models.IntegerField(null=True)),
            ],
        ),
    ]
