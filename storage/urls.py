from django.urls import path
from . import views

urlpatterns = [
    path('item', views.set_item),
    path('item/', views.get_item),
]
