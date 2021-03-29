#import user.views
from user.views import user, myPlantList, myPlantDetail, myPlantDiary
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'user', UserModelViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('login/', user.kakaoLogin ),
    path('delete/', user.deleteUser),
    path('detail/', user.getUserDetail ),
    path('myplant/add/', myPlantList.updateMyPlantAdd),
    path('myplant/mod/', myPlantList.updateMyPlantNickname),
    path('myplant/', myPlantList.getMyPlantList),
    path('myplant/del/', myPlantList.deleteMyPlant),
    path('myplant/chat/', myPlantList.getChatting),
    path('myplant/detail/<int:myplant_id>', myPlantDetail.getMyPlantDetail),
    path('myplant/repotting/',myPlantDetail.updateRepottingPoint),
    path('myplant/watering/',myPlantDetail.updateWateringPoint),
    path('myplant/mod/nickname/',myPlantDetail.modifyMyPlantNickname),
    path('diary/', myPlantDiary.getDiary),
    path('diary/add/', myPlantDiary.addDiary),
    path('diary/mod/', myPlantDiary.modifyDiary),
    path('diary/del/', myPlantDiary.deleteDiary),
]
