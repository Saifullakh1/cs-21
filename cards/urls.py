from django.urls import path
from .views import CardAPIView


urlpatterns = [
    path('create', CardAPIView.as_view(), name='create')
]