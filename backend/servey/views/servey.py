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

@api_view(['GET'])
def getServeyQuestion(request):
    question_list = []
    sql = "select * from servey"
    curs.execute(sql)
    question_list = curs.fetchall()
    return JsonResponse({'message':'success', 'question_list':question_list},status = 200)
    