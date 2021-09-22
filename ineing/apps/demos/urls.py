from django.urls import path
from .views import hello_world, HelloWorldView, ExampleView, CategoriaView, CategoriaDetailView

app_name = 'demos'

urlpatterns = [
    path('hello-world/', hello_world),
    path('hello-class/', HelloWorldView.as_view()),
    path('example/<int:code>/', ExampleView.as_view()),
    path('categorias/', CategoriaView.as_view()),
    path('categorias/<int:id>/', CategoriaDetailView.as_view()),
]
