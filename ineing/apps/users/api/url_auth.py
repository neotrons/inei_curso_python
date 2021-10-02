from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

app_name = 'api_auth'

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('verify/', verify_jwt_token)
]
