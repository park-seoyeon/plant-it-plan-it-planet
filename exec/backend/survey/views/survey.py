import requests
import json
import jwt
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from backend.settings import conn
from backend.my_settings import JWT_SECRET_KEY, JWT_ALGORITHM, KAKAO_API_KEY
from survey.models.survey import Survey

curs = conn.cursor(pymysql.cursors.DictCursor)

# 설문조사 문항 가져오기
@api_view(['GET'])
def getSurveyQuestion(request):
    question_list = []
    sql = "select * from survey"
    curs.execute(sql)
    question_list = curs.fetchall()
    return JsonResponse({'message':'success', 'question_list':question_list},status = 200)


@ api_view(['POST'])
def isSurvey(request):
    data = json.loads(request.body)
    user_number = data['user_number']

    sql = """select survey from user
            where user_number = %s"""
    curs.execute(sql, user_number)
    result = curs.fetchall()[0]['survey']

    return JsonResponse({'survey': result}, status=200)