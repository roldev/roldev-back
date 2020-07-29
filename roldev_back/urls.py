"""roldev_back URL Configuration"""

from django.contrib import admin
from django.urls import path, include

def keep_alive(request):
    return HttpResponse()

urlpatterns = [
    path('', include('leads.urls')),
    path('keep-alive/', keep_alive),
]
