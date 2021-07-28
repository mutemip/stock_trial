from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('stocks/', views.add_stock, name="add_stock"),
    path('delete/<stocks_id>/', views.delete, name='delete'),
    path('delete_stocks/', views.delete_stock, name="delete_stock")
]
