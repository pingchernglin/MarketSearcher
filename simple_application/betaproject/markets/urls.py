from django.urls import path, include
from . import views

urlpatterns = [
    path('markets/', views.markets, name='markets'),
    path('get_update/', views.get_update, name='get_update'),
    path('filter_time/', views.filter_time, name='filter_time'),
    path('filter_address/', views.filter_address, name='filter_address'),
]