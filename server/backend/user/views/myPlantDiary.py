import requests
import json
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from backend.settings import conn
from parse import *
from datetime import datetime, timedelta

curs = conn.cursor(pymysql.cursors.DictCursor)

# 식물일지 작성
@api_view(['POST'])
def addDiary(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    myplant_id = data['myplant_id']
    title = data['title']
    content = data['content']
    sql = """insert into diary (user_plant_id, user_number, title, content, add_date)
            values (%s, %s, %s, %s, now())"""
    curs.execute(sql, (myplant_id, user_number, title, content))
    conn.commit()

    
    # [My Planet Reward6 : 너와의 추억]
    sql = """update user_reward
            set reward_cnt = if( 
                                (select count(*) 
                                    from diary
                                    where user_number = %s)>=5, if(reward6=0, reward_cnt+1, reward_cnt), reward_cnt
                                ),
                reward6 = if(
                                (select count(*) 
                                    from diary
                                    where user_number = %s)>=5, 1, reward6
                                )
            where user_number=%s"""
    curs.execute(sql, (user_number, user_number, user_number))
    conn.commit()
    
    return JsonResponse({'message':'success'}, status = 200)


# 식물일지 보기
@api_view(['POST'])
def getDiary(request):
    data = json.loads(request.body)
    myplant_id = data['myplant_id']
    sql = "select * from diary where user_plant_id = %s order by id desc"
    curs.execute(sql, myplant_id)
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