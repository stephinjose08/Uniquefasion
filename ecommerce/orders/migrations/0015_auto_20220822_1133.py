# Generated by Django 3.2.14 on 2022-08-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_order_couponaplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canceled_orders',
            name='cancel_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('confirmed', 'confirmed'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('canceled', 'canceled'), ('returned', 'returned')], default='confirmed', max_length=50),
        ),
        migrations.AlterField(
            model_name='returned_orders',
            name='return_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
