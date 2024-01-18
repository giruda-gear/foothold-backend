from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.get_materials, name='get-meterials'),
]