from django.urls import path
from .templates.views import home

urlpatterns = [
    path('', home, name='home'),
]