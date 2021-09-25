from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet

app_name = 'api_demos'

router = DefaultRouter()
router.register(r'categoria', CategoriaViewSet)

urlpatterns = router.urls
