from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.set_item),
    path('item/get/', views.get_item),
]