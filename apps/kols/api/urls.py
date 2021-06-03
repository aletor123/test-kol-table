from rest_framework.routers import DefaultRouter

from .views import KolViewSet

app_name = 'kols_api'

router = DefaultRouter()
router.register('kols', KolViewSet)

urlpatterns = router.urls
