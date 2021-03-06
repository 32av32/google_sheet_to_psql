# Generated by Django 4.0.5 on 2022-06-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, verbose_name='№')),
                ('order_num', models.CharField(max_length=7, unique=True, verbose_name='Номер заказа')),
                ('price', models.FloatField(verbose_name='Стоимость')),
                ('delivery_time', models.DateField(verbose_name='Дата поставки')),
                ('price_rouble', models.FloatField(verbose_name='Стоимость в руб.')),
            ],
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['delivery_time'], name='delivery_time_idx'),
        ),
    ]
