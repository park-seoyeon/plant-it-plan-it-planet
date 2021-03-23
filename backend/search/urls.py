from search.views import search
from django.urls import path, include

urlpatterns = [
    path('', search.getSearchList ),
]