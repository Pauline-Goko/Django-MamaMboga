# Generated by Django 4.2.3 on 2023-07-10 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_payment_refunds'),
        ('order', '0013_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
    ]
