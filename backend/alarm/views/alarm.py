import os
import django
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
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
from user.views import myPlantList
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

curs = conn.cursor(pymysql.cursors.DictCursor)


def my_job():
    sql = "select * from user"
    curs.execute(sql)
    user_list = curs.fetchall()
    for user in user_list:
        refreshToken(user['kakao_refresh_token'], user['user_number'])

    sql = "select * from user_plant"
    curs.execute(sql)
    plants_list = curs.fetchall()
    receiver_list = []

    for plant in plants_list:
        if plant['last_watering_date']:
            if myPlantList.getWaterPC(plant['last_watering_date'], plant['watering_period'])[1] == 0:
                receiver_list.append(
                    [plant['user_number'], plant['plant_nickname']])

    for receiver in receiver_list:
        sql = "select email, kakao_access_token, kakao_refresh_token from user where user_number = " + \
            str(receiver[0])
        curs.execute(sql)
        token = curs.fetchall()

        new_token = refreshToken(token[0]['kakao_refresh_token'], str(receiver[0]))[
            'access_token']

        email = token[0]['email']
        sendToMeMessage(
            "오늘은 " + receiver[1] + " 물 주는 날!", new_token, "water", receiver[1])
        sender(email, "오늘은 " + receiver[1] + " 물 주는 날!", receiver[1])


# DB 갔다와야됨 -> id로 kakao access token 가져오기
def sendToMeMessage(text, kakao_access_token, type, name):
    header = {"Authorization": 'Bearer ' + kakao_access_token}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"  # 나에게 보내기 주소

    if type == "water":
        post = {
            "object_type": "feed",
            "content": {
                "title": text,
                "description": name,
                "image_url": "https://postfiles.pstatic.net/MjAyMTA0MDZfMTUx/MDAxNjE3Njc2MTIzMzY5.TUzygyBY3vDoZ7aj3NYblxVOhTJiZdP2Ck9PrTVITQsg.n0DAZdeQq2V5mi_KkOEUsfFYHMP3bamG6RbjctrS0hcg.PNG.ajx0114/KakaoTalk_20210406_112751767.png?type=w773",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://j4a101.p.ssafy.io/",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
            "buttons": [
                {
                    "title": "웹으로 이동",
                    "link": {
                        "web_url": "http://j4a101.p.ssafy.io/"
                    }
                },
            ]
        }
    elif type == "talk":
        post = {
            "object_type": "feed",
            "content": {
                "title": text,
                "description": name,
                "image_url": "https://postfiles.pstatic.net/MjAyMTA0MDZfMjM2/MDAxNjE3Njc2MTIzNDY4.yexsfrSPEznrFrA3FiyK0iiw_W87q8lWCsSUDl5lHIQg.yXb-SsB9KmdlaZ7cycDZSvYI3mvB4293WOKeHCzSmfcg.PNG.ajx0114/KakaoTalk_20210406_112752106.png?type=w773",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://j4a101.p.ssafy.io/",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
            "buttons": [
                {
                    "title": "웹으로 이동",
                    "link": {
                        "web_url": "http://j4a101.p.ssafy.io/"
                    }
                },
            ]
        }
    else:
        post = {
            "object_type": "text",
            "text": text,
            "link": {
                "web_url": "https://developers.kakao.com",
            },
            "button_title": "플랜잇"
        }

    data = {"template_object": json.dumps(post)}

    return requests.post(url, headers=header, data=data)


def refreshToken(refresh_token, user_number):
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": KAKAO_API_KEY,
        "refresh_token": refresh_token
    }
    response = requests.post(url, data=data)

    refresh_token = response.json()['access_token']
    sql = "update user set kakao_access_token = %s where user_number = %s"
    curs.execute(sql, (refresh_token, user_number))

    return response.json()


def sender(email, text, name):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('plantitplanitplanet@gmail.com', 'dkdcuyjeaslswoxv')

    body = """
   <!DOCTYPE html>
<html lang="" style="margin: 0px; height: 100%">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <link
      rel="stylesheet"
      type="text/css"
      href="https://cdn.rawgit.com/moonspam/NanumSquare/master/nanumsquare.css"
    />
    <title>플랜잇</title>
  </head>

  <body
    style="
      font-family: 'NanumSquare', sans-serif;
      margin: 0px;
      height: 100%;
      text-align: center;
    "
  >
    <div
      class="content"
      style="
        width: 50%;
        background: rgb(36, 36, 36) no-repeat center center fixed;
        text-align: center;
        margin: 0 auto;
        min-height: 100%;
      "
    >
      <div style="text-align: center">
        <div style="padding: 30px 0 0 0; text-align: center">
          <div
            id="login-title"
            style="
              color: white;
              font-size: 18px;
              font-family: 'Cafe24Oneprettynight';
            "
          >
            <h1>
              <a
                href="http://j4a101.p.ssafy.io/"
                style="text-decoration: none; color: #ffffff"
                >플랜<span style="color: #00b564">'</span>잇으로 가기</a
              >
            </h1>
          </div>
        </div>
      </div>

      <div
        id="login-division-bar"
        style="
          text-align: center;
          height: 1px;
          width: 90%;
          margin: 5% auto;
          background: rgb(133, 133, 133);
        "
      ></div>

      <div
        style="
          width: 90%;
          height: 310px;
          margin: 0 auto;
          border: 2px solid white;
          border-radius: 10px;
        "
      >
        <div
          style="
            width: 97%;
            height: 280px;
            border: dashed 2px white;
            margin: 10px auto 10px auto;
            border-radius: 10px;
          "
        >
          <div
            style="
              width: 95%;
              height: 30px;
              text-align: left;
              line-height: 30px;
              color: white;
              margin: 2% 2%;
            "
          >
            FROM. """ + name + """
          </div>
          <div
            style="
              width: 95%;
              height: 210px;
              border: 1px solid white;
              margin: 0 0 10% 2%;
              color: white;
              border-radius: 10px;
              text-align: left;
            "
          >
            <div
              style="
                width: 95%;
                margin: 3% auto 0 auto;
                color: white;
                line-height: 1.5;
              "
            >
              """ + text + """
            </div>
          </div>
        </div>
      </div>

      <div
        id="login-division-bar"
        style="
          text-align: center;
          height: 1px;
          width: 90%;
          margin: 5% auto;
          background: rgb(133, 133, 133);
        "
      ></div>
      <div
        id="login-logo-text"
        style="
          color: white;
          text-align: left;
          margin: 5% 0 5% 10%;
          font-size: 17px;
        "
      >
        <b style="color: #00b564; margin: 5% 2% 10% 17%; font-size: 22px"
          >"Plant it"</b
        >
        나만의 식물을 추천받아 <br />
      </div>
      <div
        id="login-logo-text"
        style="
          color: white;
          text-align: left;
          margin: 5% 0 5% 10%;
          font-size: 17px;
        "
      >
        <b style="color: #00b564; margin: 5% 2% 5% 17%; font-size: 22px"
          >"Plan it"</b
        >
        체계적으로 관리하고 <br />
      </div>
      <div
        id="login-logo-text"
        style="
          color: white;
          text-align: left;
          margin: 5% 0 5% 10%;
          font-size: 17px;
        "
      >
        <b style="color: #00b564; margin: 5% 2% 5% 17%; font-size: 22px"
          >"Planet"</b
        >
        행성을 가꾸어 나가요 <br />
      </div>
      <div
        id="login-division-bar"
        style="
          text-align: center;
          height: 1px;
          width: 90%;
          margin: 5% auto;
          background: rgb(133, 133, 133);
        "
      ></div>
    </div>
  </body>
</html>
    """

    msg = MIMEMultipart('alternative')

    msg['Subject'] = u'플랜잇'
    msg['From'] = u'PLANET'
    msg['To'] = email
    msg.attach(MIMEText(body, 'html'))
    server.send_message(msg)

    server.quit()


scheduler = BackgroundScheduler()
intervalTrigger = IntervalTrigger(hours=5)
scheduler.add_job(my_job, intervalTrigger, id='my_job_id')
scheduler.start()
