from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.post_list, name='post_list',)
]