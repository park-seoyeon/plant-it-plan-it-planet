from django.contrib import admin
from django.urls import path, include
from alarm.views import alarm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('survey/', include('survey.urls')),
    path('search/', include('search.urls')),
    path('alarm/', include('alarm.urls')),
]
