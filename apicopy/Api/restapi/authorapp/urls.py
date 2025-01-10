from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AuthorViewSet

router = DefaultRouter()
router.register('',AuthorViewSet,basename='authorapp')
app_name = 'authorapp'

urlpatterns = [
    path('',include(router.urls))
]

