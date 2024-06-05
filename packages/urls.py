from django.urls import path;
from packages.views import index;

urlpatterns = [
    path('', index)
]
