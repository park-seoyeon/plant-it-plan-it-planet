import requests
import json
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from backend.settings import conn
from parse import *
from datetime import datetime, timedelta

curs = conn.cursor(pymysql.cursors.DictCursor)
user_level = [1, 4, 7, 10, 12]
user_title = ["식물 집사", "정원사", "식물 박사", "엘프", "땅의 여신 데메테르"]


# 유저의 my planet 정보 보내기
@api_view(['POST'])
def getMyPage(request):
    data = json.loads(request.body)
    user_number = data['user_number']

    sql = "select * from user_reward where user_number=%s"
    curs.execute(sql, user_number)
    reward = curs.fetchall()[0]
    reward_cnt = reward['reward_cnt']  # 뱃지 개수

    # 유저 정보 가져오기
    sql = "select * from user where user_number=%s"
    curs.execute(sql, user_number)
    user = curs.fetchall()[0]

    # [My Planet Reward10 : 플랜잇과 365일]
    if reward['reward10'] == 0:
        join_date = user['join_date']
        if ((join_date + timedelta(days=365)) - datetime.now()).days <= 0:
            reward_cnt += 1  # reward_cnt 증가
            sql = "update user_reward set reward10=1, reward_cnt=reward_cnt+1 where user_number=%s"
            curs.execute(sql, user_number)
            conn.commit()

    # level 및 level percentage 계산
    level = 0
    title = "일반인"
    level_pc = 0
    for i in range(5):
        if reward_cnt >= user_level[i]:
            title = user_title[i]
            level = i+1
    if level == 5:
        reward_cnt = 0
        max_reward_cnt = 0
        level_pc = 100
    elif level == 0:
        max_reward_cnt = user_level[0]
        level_pc = round(reward_cnt * 100 / max_reward_cnt, 2)
    else:
        reward_cnt = reward_cnt - user_level[level-1]
        max_reward_cnt = user_level[level]-user_level[level-1]
        level_pc = round(reward_cnt * 100 / max_reward_cnt, 2)

    level = {'level': level, 'title': title, 'reward_cnt': reward_cnt,
             'max_reward_cnt': max_reward_cnt, 'level_pc': level_pc}
    # [My Planet Reward12 : 식물아일체]
    if title == user_title[4] and reward['reward12'] == 0:
        sql = "update user_reward set reward12=1, reward_cnt=reward_cnt+1 where user_number=%s"
        curs.execute(sql, user_number)
        conn.commit()

    # 리턴 정리
    del(reward['user_number'])
    del(reward['reward_cnt'])
    del(reward['reward11_1'])
    del(reward['reward11_2'])
    del(reward['reward11_3'])
    del(reward['reward11_4'])
    del(reward['reward11_5'])
    return JsonResponse({'name': user['name'], 'profile_image': user['profile_image'], 'level': level, 'reward': reward}, status=200)
