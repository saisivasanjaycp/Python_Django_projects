from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import TaskViewSet,UserViewSet,TaskDisplayView

router=DefaultRouter()

router.register(r'dailytask',TaskViewSet)
router.register(r'User',UserViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('all',TaskDisplayView.as_view(),name='dailytask-view')
]
