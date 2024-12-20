# Generated by Django 5.1.4 on 2024-12-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_alter_factory_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, related_name='individual_entrepreneur_Product', to='shops.product', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, related_name='retail_network_Product', to='shops.product', verbose_name='Продукты'),
        ),
    ]