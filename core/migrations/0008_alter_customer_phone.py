# Generated by Django 5.0 on 2024-01-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_customer_email_alter_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
