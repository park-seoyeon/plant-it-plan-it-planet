import requests
import json
import jwt
import pymysql
from backend.my_settings import JWT_SECRET_KEY, JWT_ALGORITHM, KAKAO_API_KEY
from backend.settings import conn
from rest_framework import viewsets
from user.models.user import User
from django.http import JsonResponse
from rest_framework.decorators import api_view

curs = conn.cursor(pymysql.cursors.DictCursor)


@api_view(['POST'])
def kakaoLogin(request):
    # code로 토큰 받기
    data = json.loads(request.body)
    code = data['code']
    redirectUrl = 'http://j4a101.p.ssafy.io'  # 로컬
    # redirectUrl = 'http://j4a101.p.ssafy.io' # 서버
    url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={KAKAO_API_KEY}&redirect_uri={redirectUrl}&code={code}'
    res = requests.post(url)
    kakao_access_token = res.json().get("access_token")
    kakao_refresh_token = res.json().get("refresh_token")

    # 토큰으로 사용자 정보 받기
    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {kakao_access_token}"},
    )
    profile_json = profile_request.json()
    kakao_account = profile_json['kakao_account']

    name = kakao_account['profile']['nickname']
    email = kakao_account['email']
    profile_image = ""
    if 'profile_image_url' in kakao_account['profile']:
        profile_image = kakao_account['profile']['profile_image_url']

    # 기존 회원인지 확인
    user_number = 0
    user = getUser(email)
    if len(user) == 0:
        # 새 회원인 경우 DB 저장
        sql = """insert into user (email, name, kakao_access_token, kakao_refresh_token)
                        values (%s, %s, %s, %s)"""
        curs.execute(
            sql, (email, name, kakao_access_token, kakao_refresh_token))
        conn.commit()
        user = getUser(email)
        is_servey = 0
        # 새 회원인 경우 user_reward에도 생성
        sql = """insert into user_reward (user_number)
                        values (%s)"""
        curs.execute(sql, user[0]['user_number'])
        conn.commit()

    # 카카오 프로필 이미지 DB저장 (로그인 할 때 마다 프로필사진이 변경되었으면 반영되도록)
    user_number = user[0]['user_number']
    sql = """update user set profile_image=%s
            where user_number=%s"""
    curs.execute(sql, (profile_image, user_number))
    conn.commit()

    # 설문조사 여부 가져오기
    sql = "select survey from user where user_number=%s"
    curs.execute(sql, user_number)
    is_survey = curs.fetchall()[0]['survey']

    # jwt 토큰 생성
    access_token = jwt.encode({'email': email}, JWT_SECRET_KEY, JWT_ALGORITHM)

    return JsonResponse({'message': 'success', 'access_token': access_token, 'user_number': user_number, 'email': email, 'name': name, 'is_survey': is_survey}, status=200)


@api_view(['DELETE'])
def deleteUser(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    sql = """delete from diary
            where user_number = %s """
    curs.execute(sql, user_number)
    conn.commit()
    sql = """delete from user
            where user_number = %s """
    curs.execute(sql, user_number)
    conn.commit()
    sql = """delete from user_detail
            where user_number = %s """
    curs.execute(sql, user_number)
    conn.commit()
    sql = """delete from user_plant
            where user_number = %s """
    curs.execute(sql, user_number)
    conn.commit()
    sql = """delete from user_reward
            where user_number = %s """
    curs.execute(sql, user_number)
    conn.commit()
    return JsonResponse({'message': 'success'}, status=200)


def getUser(email):
    sql = "select * from user where email=%s"
    curs.execute(sql, email)
    user = curs.fetchall()
    return user


@api_view(['POST'])
def getUserDetail(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    sql = "select * from user_detail where user_number = %s"
    curs.execute(sql, user_number)
    user_detail = curs.fetchall()

    if not user_detail:
        user_detail = {"user_number": -1}
    else:
        user_detail = user_detail[0]

    return JsonResponse(user_detail, status=200)
