from rest_framework import serializers
from .models import StorageItem, User


class StorageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageItem
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'