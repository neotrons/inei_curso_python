from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from ..models import Categoria, Item
from .serializers import CategoriaSerializer, ItemSerializer, CustomSerializer


class CategoriaViewSet(ModelViewSet):
    """
    /api/v1/demos/categoria/ => GET(list) POST(Create)
    /api/v1/demos/categoria/:id => PUT(update) PATCH(update) GET(RETREIVE) DELETE(delete)
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ItemViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CustomViewSet(GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = CustomSerializer

    def list(self, request, *args, **kwargs):
        datos = self.get_queryset()
        serializer = self.get_serializer(datos, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return [{
            "id": 1,
            "codigo": "xxxxxxx"
        }]
