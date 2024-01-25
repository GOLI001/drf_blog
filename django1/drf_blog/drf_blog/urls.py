"""
URL configuration for drf_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/blog-auth/',
         include('rest_framework.urls')),

    path('api/v1/posts/',
         PostListCreateView.as_view(),
         name='post-list-create'),   # возвращает список всех постов

    path('api/v1/post/<int:pk>/',
         PostDetailView.as_view(),
         name='post-detail'),    # возвращает определенного поста по id

    path('api/v1/comments/',
         CommentListCreateView.as_view(),
         name='comment-list-create'),  # возвращает список комментов

    path('api/v1/comments/<int:pk>/',
         CommentDetailView.as_view(),
         name='comment-detail'),  # возвращает определенного коммента по id

    path('api/v1/auth',
         include('djoser.urls')),  # регистрация пользователя для доступа входа по токенам

    re_path(r'^auth/',
            include('djoser.urls.authtoken')),  # вход на сайт по токенам или выйти из сайта
]
