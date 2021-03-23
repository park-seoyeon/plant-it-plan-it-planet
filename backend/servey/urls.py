from servey.views import servey
from django.urls import path, include

urlpatterns = [
    path('list/', servey.getServeyQuestion ),
    path('', servey.isServey),
]