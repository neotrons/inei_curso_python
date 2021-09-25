from django.db import models


class Producto(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=200)  # Field name made lowercase.
    sku = models.CharField(db_column='SKU', max_length=10)  # Field name made lowercase.
    precio = models.TextField(db_column='PRECIO')  # Field name made lowercase. This field type is a guess.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCTO'


class Stock(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='STOCK')  # Field name made lowercase.
    producto = models.ForeignKey(
        Producto,
        related_name='stocks',
        db_column='PRODUCTO_ID',
        on_delete=models.CASCADE
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STOCK'
