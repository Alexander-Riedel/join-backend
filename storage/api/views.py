from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from storage.models import StorageItem
from storage.api.serializers import StorageItemSerializer


class StorageItemView(APIView):
    def get(self, request):
        key = request.query_params.get('key')
        if not key:
            return Response({'status': 'error', 'message': 'key parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = StorageItem.objects.get(key=key)
            serializer = StorageItemSerializer(item)
            return Response({'status': 'success', 'data': serializer.data})
        except StorageItem.DoesNotExist:
            return Response({'status': 'error', 'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        key = request.data.get('key')
        value = request.data.get('value')

        if not key or not value:
            return Response({'status': 'error', 'message': 'Missing key or value'}, status=status.HTTP_400_BAD_REQUEST)

        item, created = StorageItem.objects.update_or_create(
            key=key,
            defaults={'value': value}
        )

        return Response({
            'status': 'success',
            'data': {
                'key': item.key,
                'value': item.value
            }
        }, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
