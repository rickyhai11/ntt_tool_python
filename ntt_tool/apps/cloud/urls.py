from django.conf.urls import url
from rest_framework import routers
from views import *

router = routers.SimpleRouter()
router.register(r'cloud', CloudViewSet)
router.register(r'tenant', TenantViewSet)
router.register(r'traffic', TrafficViewSet)


urlpatterns = []
urlpatterns += router.urls
