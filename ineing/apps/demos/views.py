from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Categoria


def hello_world(request):
    return render(request, "hello.html")


class HelloWorldView(TemplateView):
    template_name = "hello.html"


class ExampleView(TemplateView):
    template_name = "example.html"

    def get(self, request, *args, **kwargs):
        # aqui sobre escribimos
        print(args)
        print(kwargs)
        print(request)
        return super(ExampleView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        labels = ['jose', 'juan', 'maria', 'dia']
        code = kwargs.get('code')
        kwargs.update({"name": labels[code]})
        return super(ExampleView, self).get_context_data(**kwargs)


class CategoriaView(TemplateView):
    template_name = 'categorias.html'

    def get_context_data(self, **kwargs):
        categorias = Categoria.objects.all()
        kwargs.update({
            "categorias": categorias
        })
        return super(CategoriaView, self).get_context_data(**kwargs)


class CategoriaDetailView(TemplateView):
    template_name = 'categoria.html'

    def get_context_data(self, **kwargs):
        categoria_id = kwargs.get('id')
        categoria = Categoria.objects.filter(id=categoria_id).first()
        kwargs.update({
            "categoria": categoria
        })
        return super(CategoriaDetailView, self).get_context_data(**kwargs)
