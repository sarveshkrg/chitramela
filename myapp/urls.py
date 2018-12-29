from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.index, name='index'),
]