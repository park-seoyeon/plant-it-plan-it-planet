import requests
import json
import jwt
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from backend.settings import conn

curs = conn.cursor(pymysql.cursors.DictCursor)


# 필터 검색
@api_view(['POST'])
def getFilterSearchList(request):
    data = json.loads(request.body)
    # 선택된 filter
    selected_list = data['selected_list']
    
    # 선택된 filter의 property명 가져오기
    selected_property_list = []
    property_sql = ""
    pCnt = 0
    for i in range(len(selected_list)):
        if selected_list[i]!=5:
            pCnt+=1
            property_sql += str(selected_list[i])+","
    if pCnt!=0:
        property_sql = property_sql[0:len(property_sql)-1]
        property_sql = " where id in ("+property_sql+")"
        sql = "select property from filter_property"+property_sql
        curs.execute(sql)
        selected_property_list = curs.fetchall()

    # 선택된 property명 사용해서 식물 가져오기
    filter_sql = ""
    if len(selected_property_list)!=0:
        # 선택된 filter가 있을 경우 where절 작성
        filter_sql += " where "
        for i in range(len(selected_property_list)):
            filter_sql += str(selected_property_list[i]['property']) + " =1 and "
        filter_sql = filter_sql[0:len(filter_sql)-4]

    sql = """ select id, plant_name
            from plants_property""" + filter_sql

    curs.execute(sql)
    plant_list = curs.fetchall()
    return JsonResponse({'plant_list':plant_list},status=200)


# 단어 검색
@api_view(['GET'])
def getWordSearchList(request, word):
    
    sql = """select id, plant_name
            from plants_property
            where plant_name like '%"""+word+"%'"
    curs.execute(sql)
    plant_list = curs.fetchall()
    return JsonResponse({'plant_list':plant_list},status=200)


# 식물 상세 페이지
@api_view(['GET'])
def getPlantDetail(request, plant_id):
    sql = "select * from plants where id=%s"
    curs.execute(sql, plant_id)
    result = curs.fetchall()[0]

    for i in range(1,9):
        temp_sos = "sos_"+str(i)
        temp_sol = "sos_solution_"+str(i)
        if result[temp_sos]=="":
            del(result[temp_sos])
            del(result[temp_sol])
    return JsonResponse({'result':result},status = 200)


# 'my plant'에 식물 추가 (내 식물로 추가하기, 키우기 시작X)
@api_view(['POST'])
def addMyPlant(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    plant_id = data['plant_id']
    # plant_nickname은 우선 plant_name으로 기본설정
    sql = """insert into user_plant (user_number, plant_id, plant_nickname, plant_name)
            values (%s, %s, (
                                select plant_name
                                from plants
                                where id=%s
                            ),
                            (
                                select plant_name
                                from plants
                                where id=%s
                            )

             )"""
    curs.execute(sql, (user_number, plant_id, plant_id, plant_id))
    conn.commit()
    return JsonResponse({'message':'success'}, status=200)