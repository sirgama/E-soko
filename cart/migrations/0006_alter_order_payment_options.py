# Generated by Django 3.2 on 2022-07-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_order_payment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_options',
            field=models.BooleanField(choices=[('M-Pesa', 'M-Pesa'), ('PayPal', 'PayPal'), ('Stripe', 'Stripe')], default=False),
        ),
    ]