from django.urls import path
from .templates.views import home, feedback

urlpatterns = [
    path('', home, name='home'),
    path('feedback/', feedback, name='feedback')
]
