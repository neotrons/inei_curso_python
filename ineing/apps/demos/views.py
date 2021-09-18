from django.shortcuts import render
from django.views.generic import TemplateView


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
