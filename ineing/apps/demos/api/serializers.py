from rest_framework import serializers
from ..models import Categoria, Item


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    categoria = serializers.SlugRelatedField(slug_field='nombre', read_only=True)
    price_without_igv = serializers.FloatField(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'codigo', 'nombre', 'stock', 'price', 'price_without_igv', 'categoria')
