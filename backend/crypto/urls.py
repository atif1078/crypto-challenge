from django.contrib import admin
from django.urls import path
from .views import MyAPIView

urlpatterns = [
    path('api/crypto/(?P<currency>\w+)/$', MyAPIView.as_view(), name='my-view'),
    path('api/crypto', MyAPIView.as_view(), name='my-view'),
]
