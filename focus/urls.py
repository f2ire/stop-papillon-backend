from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SessionViewSet, ProtectedView

router = DefaultRouter()
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("protected/", ProtectedView.as_view(), name = "protected"),
]