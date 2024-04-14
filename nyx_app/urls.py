from django.urls import path
from .templates.views import home, feedback, companies

urlpatterns = [
    path('', home, name='home'),
    path('feedback/', feedback, name='feedback'),
    path('companies/', companies, name='companies')
]
