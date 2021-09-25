from django.db import models


class UnidadMedida(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='nombre')

    class Meta:
        db_table = "UNIDAD_MEDIDA"

    def __str__(self):
        return self.name


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Item(models.Model):
    MEDIDA_CHOICES = (
        (1, 'UNIDAD'),
        (2, 'KILOGRAMO'),
        (3, 'MILILITROS'),
    )
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    price = models.FloatField()
    categoria = models.ForeignKey(
        Categoria,
        related_name='items',
        on_delete=models.CASCADE
    )
    sumary = models.TextField(null=True, blank=True)
    unidad_medida = models.PositiveSmallIntegerField(choices=MEDIDA_CHOICES)
    activo = models.BooleanField(default=True)
    tiene_igv = models.BooleanField(default=False)

    def __str__(self):
        return self.codigo


class Proveedor(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=100)  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVEEDOR'
