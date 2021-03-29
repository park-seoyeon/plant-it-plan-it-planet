import requests
import json
import jwt
import pymysql
from config.my_settings import JWT_SECRET_KEY, JWT_ALGORITHM, KAKAO_API_KEY
from config.settings import conn
from rest_framework import viewsets
from user.models.user import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
# from user.serializers.user import UserSerializer

# class UserModelViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

curs = conn.cursor(pymysql.cursors.DictCursor)

@api_view(['POST'])
def kakaoLogin(request):
    # code로 토큰 받기
    data = json.loads(request.body)
    code = data['code']
    redirectUrl = 'http://localhost:8080'
    url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={KAKAO_API_KEY}&redirect_uri={redirectUrl}&code={code}'
    res = requests.post(url)
    kakao_access_token = res.json().get("access_token")

    # 토큰으로 사용자 정보 받기
    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {kakao_access_token}"},
    )
    profile_json = profile_request.json()
    kakao_account = profile_json['kakao_account']
    name = kakao_account['profile']['nickname']
    email = kakao_account['email']
    profile_image = kakao_account['profile']['profile_image_url']
    print(email+ "/" +name+ "/"+profile_image)

    # 기존 회원인지 확인
    user_number = 0
    user = getUser(email)
    if len(user)==0:
        # 새 회원인 경우 DB 저장
        sql = """insert into user (email, name)
                        values (%s, %s)"""
        curs.execute(sql, (email, name))
        conn.commit()
        user = getUser(email)
    
    user_number = user[0]['user_number']

    # jwt 토큰 생성
    access_token = jwt.encode({'email':email}, JWT_SECRET_KEY, JWT_ALGORITHM)

    return JsonResponse({'message':'success', 'access_token':access_token, 'user_number':user_number, 'email':email, 'name':name, 'profile_image':profile_image}, status = 200)


@api_view(['DELETE'])
def deleteUser(request):
    data = json.loads(request.body)
    user_number = data['user_number']
    sql = """delete from user
            where user_number = %s """
    curs.execute(sql, user_number)
    conn.commit()
    return JsonResponse({'message':'success'}, status=200)


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
    
    return JsonResponse(user_detail[0], status=200)