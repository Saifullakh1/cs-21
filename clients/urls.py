from django.urls.conf import path
from .views import ClientListAPIView, ClientRetrieveAPIView


urlpatterns = [
    path('', ClientListAPIView.as_view(), name='client-list'),
    path('<int:pk>', ClientRetrieveAPIView.as_view(), name='client-detail')
]