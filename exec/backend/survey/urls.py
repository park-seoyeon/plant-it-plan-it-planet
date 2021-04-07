from survey.views import survey
from survey.views import mbti_recommend
from django.urls import path, include

urlpatterns = [
    path('list/', survey.getSurveyQuestion),
    path('', survey.isSurvey),
    path('result/', mbti_recommend.getSurveyAnswer),
]
