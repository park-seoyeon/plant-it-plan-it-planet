from servey.views import servey
from servey.views import mbti_recommend
from django.urls import path, include

urlpatterns = [
    path('list/', servey.getServeyQuestion),
    path('', servey.isServey),
    path('result/', mbti_recommend.getServeyAnswer),
]
