from django.urls import path
from django.views.decorators.cache import cache_page

from .views import IndexView


urlpatterns = [
    path('', cache_page(20)(IndexView.as_view()), name='index'),
]
