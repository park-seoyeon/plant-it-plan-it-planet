from search.views import search
from django.urls import path, include

urlpatterns = [
    path('', search.getFilterSearchList),
    path('<str:word>', search.getWordSearchList),
    path('detail/<int:plant_id>', search.getPlantDetail),
    path('add/', search.addMyPlant),
]