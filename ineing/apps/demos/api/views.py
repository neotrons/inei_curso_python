from rest_framework import mixins, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import action
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
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['price']

    @action(methods=['GET'], url_path='activos', detail=False)
    def actives(self, request, *args, **kwargs):
        queryset = self.queryset.filter(activo=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], url_path=r'categoria/(?P<category_id>[0-9]+)', detail=False)
    def by_category(self, request, *args, **kwargs):
        category_id = int(kwargs.get('category_id'))
        queryset = self.queryset.filter(categoria_id=category_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
