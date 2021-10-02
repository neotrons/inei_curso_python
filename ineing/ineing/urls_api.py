from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('demos/', include('apps.demos.api.urls', namespace='api_demos')),
    path('auth/', include('apps.users.api.url_auth', namespace='api_auth'))
]