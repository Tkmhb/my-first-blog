<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
=======
from importlib.resources import path
from django.urls improt path
from . import views

urlpatterns = {
    path('', views.post_list, name='post_list'),
}
>>>>>>> fa58a3ee66becd927307104db98b77f5d189c05d
