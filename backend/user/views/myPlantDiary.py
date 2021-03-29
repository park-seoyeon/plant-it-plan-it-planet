import requests
import json
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from config.settings import conn
from parse import *
from datetime import datetime, timedelta

curs = conn.cursor(pymysql.cursors.DictCursor)

# 식물일지 작성
@api_view(['POST'])
def addDiary(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    title = data['title']
    content = data['content']
    sql = """insert into diary (user_number, title, content, add_date)
            values (%s, %s, %s, now())"""
    curs.execute(sql, (user_number, title, content))
    conn.commit()
    return JsonResponse({'message':'success'}, status = 200)


# 식물일지 보기
@api_view(['POST'])
def getDiary(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    sql = "select * from diary where user_number = %s order by id desc"
    curs.execute(sql, user_number)
    diary_list = curs.fetchall()
    return JsonResponse({'diary_list':diary_list}, status=200)

# 식물일지 수정
@api_view(['PUT'])
def modifyDiary(request):
    data = json.loads(request.body)
    diary_id = data['diary_id']
    title = data['title']
    content = data['content']
    sql = """update diary set title = %s, content = %s
            where id=%s"""
    curs.execute(sql, (title, content, diary_id))
    conn.commit()
    return JsonResponse({'message':'success'}, status = 200)


# 식물일지 삭제
@api_view(['DELETE'])
def deleteDiary(request):
    data = json.loads(request.body)
    diary_id = data['diary_id']
    sql = """delete from diary
            where id=%s"""
    curs.execute(sql, diary_id)
    conn.commit()
    return JsonResponse({'message':'success'}, status = 200)