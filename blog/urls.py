from importlib.resources import path
from django.urls improt path
from . import views

urlpatterns = {
    path('', views.post_list, name='post_list'),
}