from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StorageItem
from .serializers import StorageItemSerializer


@api_view(['POST'])
def set_item(request):
    key = request.data.get('key')
    value = request.data.get('value')
    if not key or value is None:
        return Response({'error': 'Key and value required.'}, status=status.HTTP_400_BAD_REQUEST)

    item, created = StorageItem.objects.update_or_create(
        key=key, defaults={'value': value})
    serializer = StorageItemSerializer(item)
    return Response(serializer.data)


@api_view(['GET'])
def get_item(request):
    key = request.GET.get('key')
    if not key:
        return Response({'error': 'Key required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        item = StorageItem.objects.get(key=key)
        serializer = StorageItemSerializer(item)
        return Response(serializer.data)
    except StorageItem.DoesNotExist:
        return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)
