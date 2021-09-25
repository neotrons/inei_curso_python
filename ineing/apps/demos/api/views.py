from rest_framework.viewsets import ModelViewSet
from ..models import Categoria
from .serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    """
    /api/v1/demos/categoria/ => GET(list) POST(Create)
    /api/v1/demos/categoria/:id => PUT(update) PATCH(update) GET(RETREIVE) DELETE(delete)
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
