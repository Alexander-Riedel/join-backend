from django.urls import path
from storage.api.views import StorageItemView


urlpatterns = [
    path('item', StorageItemView.as_view()),
]
