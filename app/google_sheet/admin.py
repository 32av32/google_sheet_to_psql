from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'num', 'order_num', 'price', 'delivery_time', 'price_rouble')
