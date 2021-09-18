from django.urls import path
from .views import hello_world, HelloWorldView, ExampleView

app_name = 'demos'

urlpatterns = [
    path('hello-world/', hello_world),
    path('hello-class/', HelloWorldView.as_view()),
    path('example/<int:code>/', ExampleView.as_view()),
]
