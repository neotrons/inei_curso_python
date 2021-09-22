# Generated by Django 3.2.7 on 2021-09-21 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('sumary', models.TextField(blank=True, null=True)),
                ('unidad_medida', models.PositiveSmallIntegerField(choices=[(1, 'UNIDAD'), (2, 'KILOGRAMO'), (3, 'MILILITROS')])),
                ('activo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='demos.categoria')),
            ],
        ),
    ]
