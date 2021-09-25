"""ineing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.conf.urls.static import static
from .swagger import schema_view

urlpatterns = [
    re_path('^$', lambda request: redirect('swagger/', permanent=False)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('demo/', include('apps.demos.urls', namespace='demos')),
    path('api/v1/', include('ineing.urls_api', namespace='api'))
]

if settings.DEBUG:
    urlpatterns = urlpatterns \
                  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
