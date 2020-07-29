"""roldev_back URL Configuration"""

from django.contrib import admin
from django.urls import path, include

def keep_alive(request):
    return HttpResponse()

urlpatterns = [
    path('keep-alive/', keep_alive),
    path('', include('leads.urls')),
]
