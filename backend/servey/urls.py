from servey.views import servey
from django.urls import path, include

urlpatterns = [
    path('', servey.getServeyQuestion ),
]