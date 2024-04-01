from django.urls import path
from . import views

urlpatterns=[
    path('blog/create', views.create, name='create'),
    path('blog/<int:blog_id>', views.detail, name='detail'),
    path('', views.list_blogs, name='list_blogs'),
]