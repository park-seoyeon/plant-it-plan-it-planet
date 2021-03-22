#import user.views
from user.views import user
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'user', UserModelViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('login/', user.kakaoLogin ),
]