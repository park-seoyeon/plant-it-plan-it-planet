import requests
import json
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from backend.settings import conn
from parse import *
from datetime import datetime, timedelta
from user.views.myPlantList import getWaterPC, getRepottingPC

curs = conn.cursor(pymysql.cursors.DictCursor)
level = [30, 50, 100, 200, 400]

# 사용자의 식물 상세페이지 정보 가져오기


@api_view(['GET'])
def getMyPlantDetail(request, myplant_id):
    sql = "select * from user_plant where id=%s"
    curs.execute(sql, myplant_id)
    result = curs.fetchall()

    # add_date 시간 빼고 날짜만 보내기
    result[0]['add_date'] = datetime.date(result[0]['add_date'])

    # 물, 분갈이 percentage, d-day 가져오기
    last_watering_date = result[0]['last_watering_date']
    watering_period = result[0]['watering_period']
    temp = getWaterPC(last_watering_date, watering_period)
    result[0]['watering_pc'] = temp[0]
    result[0]['watering_d_day'] = temp[1]

    last_repotting_date = result[0]['last_repotting_date']
    temp = getRepottingPC(last_repotting_date)
    result[0]['repotting_pc'] = temp[0]
    result[0]['repotting_d_day'] = temp[1]

    # level percentage 계산
    point = result[0]['point']
    plant_level = result[0]['level']
    level_pc = 100
    max_point = 0
    # max level인 경우
    if plant_level <= 5:
        level_pc = round((point * 100 / level[plant_level-1]), 2)
        max_point = level[plant_level-1]
    result[0]['level_pc'] = level_pc
    result[0]['max_point'] = max_point

    return JsonResponse({'result': result[0]}, status=200)


# 물주기 버튼 클릭
@api_view(['PUT'])
def updateWateringPoint(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    myplant_id = data['myplant_id']

    sql = """ update user_plant set point=point+10, last_watering_date = now(), watering_cnt = watering_cnt+1
                where id = %s"""
    curs.execute(sql, myplant_id)
    conn.commit()

    # [My Planet Reward4 : 아이~ 맛있어..!]
    sql = """update user_reward
            set reward_cnt = if( 
                                (select sum(watering_cnt) 
                                    from user_plant
                                    where user_number = %s)>=30, if(reward4=0, reward_cnt+1, reward_cnt), reward_cnt
                                ),
                reward4 = if(
                                (select sum(watering_cnt) 
                                    from user_plant
                                    where user_number = %s)>=30, 1, reward4
                                )
            where user_number=%s"""
    curs.execute(sql, (user_number, user_number, user_number))
    conn.commit()

    # level 증가했는지 체크
    getPlantLevel(myplant_id, user_number)
    return JsonResponse({'message': 'success'}, status=200)


# 분갈이 버튼 클릭
@api_view(['PUT'])
def updateRepottingPoint(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    myplant_id = data['myplant_id']
    sql = """ update user_plant set point=point+100, last_repotting_date = now(), repotting_cnt = repotting_cnt+1
                where id = %s"""
    curs.execute(sql, myplant_id)
    conn.commit()

    # [My Planet Reward5 : 새 집 마련]
    sql = """update user_reward
            set reward_cnt = if(reward5=0, reward_cnt+1, reward_cnt), reward5=1
            where user_number=%s"""
    curs.execute(sql, user_number)
    conn.commit()

    # level 증가했는지 체크
    getPlantLevel(myplant_id, user_number)
    return JsonResponse({'message': 'success'}, status=200)


# 식물 level, percentage 계산
def getPlantLevel(myplant_id, user_number):
    sql = "select level, point from user_plant where id = %s"
    curs.execute(sql, myplant_id)
    result = curs.fetchall()
    plant_level = result[0]['level']
    point = result[0]['point']
    if plant_level > 5:
        point = 0

    # level 올랐는지 체크 및 DB반영
    for i in range(plant_level-1, 5):
        if point >= level[i]:
            if i == 4:
                plant_level = 6  # max_level
                point = 0
            else:
                plant_level = i+2
                point -= level[i]
    sql = """update user_plant set point=%s, level = %s
            where id=%s """
    curs.execute(sql, (point, plant_level, myplant_id))
    conn.commit()

    if plant_level >= 5:
        # [My Planet Reward8 : 하바드 식물학과 졸업]
        sql = """update user_reward
                set reward_cnt = if(reward8=0, reward_cnt+1, reward_cnt), reward8 = 1
                where user_number=%s"""
        curs.execute(sql, user_number)
        conn.commit()


# 식물 정보 수정 (별명 수정)
@api_view(['PUT'])
def modifyMyPlantNickname(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    myplant_id = data['myplant_id']
    plant_nickname = data['plant_nickname']

    sql = """ update user_plant set plant_nickname = %s
                where id = %s"""
    curs.execute(sql, (plant_nickname, myplant_id))
    conn.commit()

    # [My Planet Reward3 : 너의 이름은...]
    sql = """update user_reward
            set reward_cnt = if(reward3=0, reward_cnt+1, reward_cnt), reward3=1
            where user_number=%s"""
    curs.execute(sql, user_number)
    conn.commit()
    return JsonResponse({'message': 'success'}, status=200)
