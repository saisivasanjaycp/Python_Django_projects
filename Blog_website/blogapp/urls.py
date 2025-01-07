# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('createblog/', views.create_blog, name='create_blog'),
    path('', views.home, name='home'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),
    path('blogapp/<slug:slug>',views.blog_detail,name='blog_detail')
]