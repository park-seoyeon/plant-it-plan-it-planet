from user.views import user, myPlantList, myPlantDetail, myPlantDiary, myPlanet
from django.urls import path, include

urlpatterns = [
    path('login/', user.kakaoLogin),
    path('delete/', user.deleteUser),
    path('detail/', user.getUserDetail),
    path('myplant/add/', myPlantList.updateMyPlantAdd),
    path('myplant/', myPlantList.getMyPlantList),
    path('myplant/del/', myPlantList.deleteMyPlant),
    path('myplant/chat/', myPlantList.getChatting),
    path('myplant/detail/<int:myplant_id>', myPlantDetail.getMyPlantDetail),
    path('myplant/repotting/', myPlantDetail.updateRepottingPoint),
    path('myplant/watering/', myPlantDetail.updateWateringPoint),
    path('myplant/mod/nickname/', myPlantDetail.modifyMyPlantNickname),
    path('diary/', myPlantDiary.getDiary),
    path('diary/add/', myPlantDiary.addDiary),
    path('diary/mod/', myPlantDiary.modifyDiary),
    path('diary/del/', myPlantDiary.deleteDiary),
    path('mypage/', myPlanet.getMyPage),
]
