from django.urls import path
from .views import calculate_feeding

urlpatterns = [
    path('feeding/', calculate_feeding, name='feeding-calc'),
]
