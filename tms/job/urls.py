from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter(trailing_slash=False)
router.register(
    r'job', views.JobViewSet, base_name='job'
)

urlpatterns = [
    url(r'^', include(router.urls)),
]
