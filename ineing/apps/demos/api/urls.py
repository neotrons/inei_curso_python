from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ItemViewSet

app_name = 'api_demos'

router = DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'item', ItemViewSet)

urlpatterns = router.urls
