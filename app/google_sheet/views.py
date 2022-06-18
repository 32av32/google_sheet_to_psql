from django.views.generic import ListView

from .models import Order


class IndexView(ListView):
    model = Order
    queryset = Order.objects.all()
    template_name = 'index.html'
    ordering = 'num'
