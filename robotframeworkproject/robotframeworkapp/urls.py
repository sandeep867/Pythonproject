from django.urls import path
from .views import TestAutomation

urlpatterns = [
    path('tests/v1/execute/', TestAutomation, name='TestAutomation'),
]
