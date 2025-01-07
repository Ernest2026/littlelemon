from django.urls import path
from .views import little, addBook

urlpatterns = [
    path('little/', little),
    path('addBook/', addBook)
]
