from django.db import models


class Order(models.Model):
    num = models.IntegerField(verbose_name='№', blank=True)
    order_num = models.CharField(verbose_name='Номер заказа', max_length=7, unique=True)
    price = models.FloatField(verbose_name='Стоимость')
    delivery_time = models.DateField(verbose_name='Дата поставки')
    price_rouble = models.FloatField(verbose_name='Стоимость в руб.')

    class Meta:
        indexes = (models.Index(fields=('delivery_time',), name='delivery_time_idx'),)

    def __str__(self):
        return self.order_num


