from django.contrib import admin
from django.urls import path
from posts.views import post_detail, post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]