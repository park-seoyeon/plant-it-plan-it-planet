import requests
import json
import jwt
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from config.settings import conn
from config.my_settings import JWT_SECRET_KEY, JWT_ALGORITHM, KAKAO_API_KEY
#from search.models.search import Servey

curs = conn.cursor(pymysql.cursors.DictCursor)

def getFilterList(request):
    selected_list = [] # 선택된 filter
    data = json.loads(request.body)
    selected_list = data['selected_list']

    filter_list = []

    if(len(selected_list)==0):
        # selected_list 크기 0 : 아무것도 선택되지 않음 => 제일 초기의 대분류 4개 property 반환
        sql = """select * from filter_property
                where id<=4"""
        curs.execute(sql)
        filter_list = curs.fetchall()
    else:
        last_selected = selected_list[len(selected_list)-1]
        if(last_selected==5):
            sql = """ select child_property_id from filter_child
                    where peroperty_id=%s and parents_property_id=%s"""
            curs.execute(sql, (last_selected, selected_list[0]))
            result = curs.fetchall()
            print(result)
        else:
            sql = """ select child_property_id from filter_child
                    where peroperty_id=%s """
            curs.execute(sql, last_selected)
            result = curs.fetchall()
            print(result)

    return JsonResponse({'filter_list':filter_list},status=200)  

@api_view(['POST'])
def getSearchList(request):
    # 검색창, filter 선택 가져오기
    print("here")

    selected_list = [] # 선택된 filter
    last_selected = 0 # 마지막으로 선택된 filter 
    data = json.loads(request.body)
    selected_list = data['selected_list']
    last_selected = data['last_selected']

    filter_list = []
    plant_list = []

    if(len(selected_list)==0):
        # selected_list 크기 0 : 아무것도 선택되지 않음 => 제일 초기의 대분류 4개 property 반환
        sql = """select * from filter_property
                where id<=4"""
        curs.execute(sql)
        filter_list = curs.fetchall()

        sql = "select id, plant_name from plant_filter"
        curs.execute(sql)
        plant_list = curs.fetchall()

    else:
        if(last_selected!=5):
            st = "selected_list[1], selected_list[0]"
            sql = """ select child_property_id from filter_child
                    where peroperty_id=%s """
            curs.execute(sql,(selected_list[1], selected_list[0]))
            filter_list = curs.fetchall()
        else:
            # property_id = 5 (잎의 모양) 선택한 경우
            sql = """ select child_property_id from filter_child
            where peroperty_id=%s and parents_property_id=%s"""
            curs.execute(sql,(selected_list[1], selected_list[0]))
            filter_list = curs.fetchall()

        sql = """ select * from filter_property
                where  """

    return JsonResponse({'filter_list':filter_list, 'plant_list':plant_list},status=200)
