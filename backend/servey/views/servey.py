import requests
import json
import jwt
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from config.settings import conn
from config.my_settings import JWT_SECRET_KEY, JWT_ALGORITHM, KAKAO_API_KEY
from servey.models.servey import Servey

curs = conn.cursor(pymysql.cursors.DictCursor)

# 설문조사 문항 가져오기
@api_view(['GET'])
def getServeyQuestion(request):
    question_list = []
    sql = "select * from servey"
    curs.execute(sql)
    question_list = curs.fetchall()
    return JsonResponse({'message':'success', 'question_list':question_list},status = 200)


# mbti 검사 결과 보내주기
@api_view(['POST'])
def getServeyAnswer(request):
    answer_list = []
    data = json.loads(request.body)
    answer_list = data['answer_list']
    #### db에서 mbti결과 가져오기
    #### mbti 결과별로 설문결과페이지 뿌리기
    pass


# 설문조사 완료 여부 리턴하기
@api_view(['POST'])
def isServey(request):
    data = json.loads(request.body)
    email = data['email']

    sql = """select servey from user
            where email = %s"""
    curs.execute(sql, email)
    result = curs.fetchall()[0]['servey']
    return JsonResponse({'servey':result},status=200)