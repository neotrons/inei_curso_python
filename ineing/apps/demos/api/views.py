from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from ..models import Categoria, Item
from .serializers import CategoriaSerializer, ItemSerializer


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
