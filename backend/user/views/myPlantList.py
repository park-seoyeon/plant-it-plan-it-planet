import requests
import json
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from config.settings import conn
from parse import *
from datetime import datetime, timedelta
from gtts import gTTS
import playsound
import os
import time
import random

curs = conn.cursor(pymysql.cursors.DictCursor)


# 물 percentage 구하기
def getWaterPC(last_watering_date, watering_period):
    water_pc = 0
    water_d_day = 0
    gap_day = 0
    watering = [] # pc, d_day
    #last_watering_date =  datetime(2021, 3, 22, 0, 40, 5) # 테스트용 마지막으로 물 준날
    if last_watering_date!=None:
        
        today= datetime.now()
       
        #d-day
        water_d_day = ((last_watering_date + timedelta(days=watering_period)) - today).days
        print(water_d_day)
        # 물 줘야할 시기 놓친경우. 이미 지났음
        if water_d_day<0 : 
            return [0,0]

        # percentage
        gap_day = (today - last_watering_date).days
        gap_hour = round((today - last_watering_date).seconds / 3600, 2)

        # 일(day) 단위로 나타냄
        day_calc = gap_day+(float(gap_hour)/24)
        # percent구하기 : 주기 - (마지막)
        water_pc = round((float(watering_period) - day_calc)*100 / float(watering_period), 2)
        watering = [water_pc, water_d_day]
    else:
        watering = [0,0]
    return watering


# 분갈이 percentage 구하기 : 작은 화분 기준 1년
def getRepottingPC(last_repotting_date):
    repotting = []
    today= datetime.now()

    repotting_d_day = ((last_repotting_date + timedelta(days=365)) - today).days
    # 분갈이 시기 놓친경우. 이미 지났음
    if repotting_d_day<0 : 
        return [0,0]

    gap_day = (today - last_repotting_date).days
    gap_hour = round((today - last_repotting_date).seconds / 3600, 2)


    # 일(day) 단위로 나타냄
    day_calc = gap_day+(float(gap_hour)/24)
    # percent구하기 : 주기 - (마지막)
    repotting_pc = round((365 - day_calc)*100 / 365 ,2)
    repotting = [repotting_pc, repotting_d_day]
    return repotting
    
def speak(text):
    tts = gTTS(text=text, lang='ko', slow=False)
    filename = "plant_voice.mp3"
    tts.save(filename)
    playsound.playsound("plant_voice.mp3")
    os.remove("plant_voice.mp3")

#type = 0 : 일반, 1 : 물, 2 : 분갈이
@api_view(['POST'])
def getChatting(request):
    data = json.loads(request.body)
    plant_id = data['id']
    sql = "select * from user_plant where id=%s"
    curs.execute(sql, plant_id)
    user_plant = curs.fetchall()

    user_plant = user_plant[0]
    repottingPC = getRepottingPC(user_plant['last_repotting_date'])[0]
    waterPC = getWaterPC(user_plant['last_watering_date'], user_plant['watering_period'])[0]
    plant_level = user_plant['level']


    if repottingPC <= 1.00:
        sql = "select message from plant_chat where level=%s and type=2"
    elif waterPC <= 5.00:
        sql = "select message from plant_chat where level=%s and type=1"
    else:
        sql = "select message from plant_chat where level=%s and type=0"

    curs.execute(sql, plant_level)
    texts = curs.fetchall()
    text = texts[random.randrange(0, len(texts))]
    speak(text['message'])
    return JsonResponse({'message':'success'}, status=200)


# 사용자의 식물 리스트 출력
@api_view(['POST'])
def getMyPlantList(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    sql = """select * from user_plant where user_number=%s
            order by is_add desc, id"""
    curs.execute(sql, user_number)
    result = curs.fetchall()

    for i in range(len(result)):
        # 식물 키우기 시작한 경우
        if result[i]['is_add']==1:
            # 물, 분갈이 percentage, d-day 가져오기
            last_watering_date = result[i]['last_watering_date']
            watering_period = result[i]['watering_period']
            temp = getWaterPC(last_watering_date,watering_period)
            result[i]['watering_pc'] = temp[0]

            last_repotting_date = result[i]['last_repotting_date']
            temp = getRepottingPC(last_repotting_date)
            result[i]['repotting_pc'] = temp[0]

            # '함께한지 00일'
            today= datetime.now()
            add_date = result[i]['add_date']
            add_day_count = (today-add_date).days
            result[i]['add_day_count'] = add_day_count+1 # 키우기 시작한 당일부터 함께한지 1일이 되도록
            print(result[i])
        # my plant에 추가만 된 상태(키우기 시작X)
        else:
            result[i]['watering_pc'] = None
            result[i]['repotting_pc'] = None
            result[i]['add_day_count'] = None


    print(result)
    return JsonResponse({'myplant_list':result}, status=200)


# 'PLANT IT'버튼 눌렀을 때 (식물키우기 시작)
@api_view(['PUT'])
def updateMyPlantAdd(request):
    data = json.loads(request.body)
    myplant_id = data['myplant_id'] # user_plant 테이블의 id
    plant_name = data['plant_name'] # 실제 식물 이름
    plant_nickname = data['plant_nickname'] # 식물 별명

    # 별명 설정 안 한 경우 => 별명 = 식물 기본 이름
    if plant_nickname=="":
        plant_nickname = plant_name

    sql = """select summary_water_title from plants 
            where id = (
                            select plant_id from user_plant
                            where id =%s
                        )"""
    curs.execute(sql, myplant_id)
    summary_water_title = curs.fetchall()[0]['summary_water_title']

    # 물 주는 주기 구하기 : 주/월/회 문자열 파싱
    watering_period = 0
    result = parse("{week}주 {weekly_cnt}회",summary_water_title )
    if result==None:
        result = parse("주 {weekly_cnt}회",summary_water_title )
        if result==None:
            result = parse("월 {monthly_cnt}회",summary_water_title )
            watering_period = round(30 / int(result['monthly_cnt']),1)
        else :
            watering_period = round(7 / int(result['weekly_cnt']),1)
    else:
        watering_period = round(int(result['week'])*7 / int(result['weekly_cnt']),1)
    
    # db에 반영하기
    sql = """update user_plant
            set plant_nickname = %s, is_add = 1, add_date = now(), level = 1, point = 0, last_repotting_date = now(), 
            watering_period =%s
            where id=%s"""
    curs.execute(sql, (plant_nickname, watering_period, myplant_id))
    conn.commit()
    return JsonResponse({'message':'success'},status=200)


# 별명 변경하기
@api_view(['PUT'])
def updateMyPlantNickname(request):
    data = json.loads(request.body)
    myplant_id = data['myplant_id']
    plant_nickname = data['plant_nickname']

    sql = """update user_plant set plant_nickname=%s 
            where id = %s"""
    curs.execute(sql, (plant_nickname, myplant_id))
    conn.commit()
    return JsonResponse({'message':'success'}, status=200)


# 내 식물 삭제
@api_view(['DELETE'])
def deleteMyPlant(request):
    data = json.loads(request.body)
    myplant_id = data['myplant_id']
    sql = "delete from user_plant where id=%s"
    curs.execute(sql, myplant_id)
    conn.commit()
    return JsonResponse({'message':'success'}, status = 200)