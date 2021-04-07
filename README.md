<u>**빅데이터 특화 프로젝트**</u>

**<u>SSAFY 4기 1반 1팀 ENable</u>**

# 플랜'잇

## Plant It. Plan It. Planet.

##### Plant It. 나만의 식물을 추천받아

##### Plan It. 체계적으로 관리하고

##### Planet. 행성을 가꾸어 나가요.

![메인로고](https://user-images.githubusercontent.com/26132746/113850720-b7a7fc80-97d5-11eb-90b1-9263702cb26a.JPG)

###### **<u>MBTI 성향 조사 ( 빅데이터 )</u>** 를 기반으로 당신과 비슷한 성향의 식물이 무엇인지 알아보고,

###### 당신에게 딱 맞는 식물을 추천받아 물주기, 분갈이, 말걸기 기능을 활용해 체계적으로 관리하고,

###### 식물 별로 식물일지도 쓰고, 다양한 뱃지들도 모아 당신만의 행성을 깨끗하게 가꾸어 나가요.

------



### 목차

1. 팀원 소개
2. 프로젝트 기획배경
3. 사용한 기술스택
4. 메인 기능 소개
5. Frontend 실행방법 및 유의사항
6. Backend 실행방법 및 유의사항
7. Server 실행방법 및 유의사항



------



##### 1. 팀원 소개



- 팀장

  안준웅 ( ENTJ ) : Backend, Bigdata, Server

- 팀원

  송현아 ( ENTJ ) : Backend, DB

  신재복 ( ENFP ): Backend, ML

  최준호 ( ENFP ): Frontend

  박서연 ( ENTP ): Frontend, Design

  

**EN으로 시작하는 우리들!**

**ENable 취업도 프로젝트도 무엇이든 할 수 있다!**



------



##### 2. 프로젝트 기획배경



![식물키우기](https://user-images.githubusercontent.com/26132746/113860279-d19b0c80-97e0-11eb-939d-660c31693e60.JPG)



- 코로나 블루의 해소
- 나의 라이프 스타일에 맞는 식물
- 실내 공기청정 및 환경 개선
- 나의 식물에 대한 정보 부족
- 식물 관리 서비스 부족
- 단순히 식물을 기른다는 지루함



**==> 플랜'잇을 통해 모두 해결 !**



------



##### 3.  사용한 기술스택



- **Backend**

  <u>Django</u>, MySQL, JWT, Postman, PyMySQL

- **Frontend**

  <u>Vue.js</u>, HTML, CSS, Javascript

- **BigData**

  Jupyter Notebook, Google Colab, Scikit-learn

- **Environment**

  Ubuntu, <u>Docker</u>, <u>AWS EC2</u>, Windows Terminal

- **Collaboration-Tool**

  <u>Slack</u>, Notion, <u>Jira</u>, <u>GitLab</u>, Mattermost



------



##### 4. 메인 기능 소개



- **Main**

  **MY PLANT** : 내 식물 리스트에 추가한 식물들을 볼 수 있고,

  식물을 선택하면 해당 식물의 Myplant 관리 페이지로 이동합니다.

  **FOR YOU** : MBTI 성향조사 결과를 통해 추천받은 식물들을 보여줍니다.

  **MAGAZINE** : 식물 키우기와 관련된 잡지 소식을 전해줍니다.

<img src = "https://user-images.githubusercontent.com/26132746/113856811-b4643f00-97dc-11eb-8a9b-36827db986d9.JPG" width="30%" height="30%">



- **Search**

  필터 및 검색 기능을 이용한 식물검색 기능

  <img src = "https://user-images.githubusercontent.com/26132746/113857230-3b191c00-97dd-11eb-8b6d-926ad9fb6797.JPG" width="30%" height="30%">



- **SearchDetail**

  검색 페이지에서 선택한 식물에 대한 세부내용을 조회할 수 있고,

  '**+ 내 식물로 추가하기**' 버튼을 이용해 Myplant에 추가해 관리할 수 있습니다.

<img src = "https://user-images.githubusercontent.com/26132746/113860395-f1323500-97e0-11eb-99f4-97bbc95b464f.JPG" width="80%" height="80%">



- **Myplant**

  추가했던 식물들을 관리할 수 있는 페이지

  BUY IT 버튼을 통해 네이버 쇼핑의 해당 식물 구입정보로 연동

  PLANT IT 버튼을 통해 원하는 사진을 등록하고, 이름을 설정하여 식물을 심을 수 있습니다.

<img src = "https://user-images.githubusercontent.com/26132746/113857524-95b27800-97dd-11eb-89b0-dc09fb66979b.JPG" width="30%" height="30%">



- **MyplantDetail**

  **물주기** : 식물마다 정해져있는 적정시기에 물을 줄 수 있도록 알림제공 및 시각화

  **분갈이** : 식물마다 정해져있는 적정시기에 분갈이를 할 수 있도록 알림제공 및 시각화

  **말걸기** : 말걸기를 통해 카카오톡, 이메일로 식물과의 대화내용 전송 

  ( 식물 각각의 LV마다 대화 할 수 있는 내용이 다름 )

  <img src = "https://user-images.githubusercontent.com/26132746/113857751-db6f4080-97dd-11eb-9ba7-e39b3281f205.JPG" width="30%" height="30%">

  

  **물주기 실패 alert, 분갈이 실패 alert, 말걸기 alert**

  <img src = "https://user-images.githubusercontent.com/26132746/113860456-07d88c00-97e1-11eb-82f7-d6c4c0921c4e.JPG" width="100%" height="100%">

  

  **말걸기 기능 사용 시 발송되는 E-mail 및 카카오톡 알림 내용**

  <img src = "https://user-images.githubusercontent.com/26132746/113860637-36566700-97e1-11eb-9252-1d02638aeed5.JPG" width="100%" height="100%">



-  **PLANET**

  개인 계정 LV ( 뱃지 개수에따라 LV 증가 ) 을 확인할 수 있고,

  MBTI 성향조사 다시하기, 로그아웃, 회원탈퇴 기능 제공

  **MY PLANET** 에서는 개개인의 계정 LV에 따른 행성의 정화도 관련 이미지 제공

  ( LV이 높을수록 행성이 깨끗해집니다. )

<img src = "https://user-images.githubusercontent.com/26132746/113857987-28531700-97de-11eb-9632-ecb0494536cb.JPG" width="30%" height="30%">



- **Reward**

  다양한 조건들을 만족하면 얻을 수 있는 뱃지들을 제공

  뱃지를 얻는 성취감과 함께 개인 계정의 Levelling 에 영향을 줍니다.

<img src = "https://user-images.githubusercontent.com/26132746/113858177-66503b00-97de-11eb-8f32-1a0a75915b5d.JPG" width="30%" height="30%">



##### 5. Frontend 실행방법 및 유의사항



- git clone 받아올 경우 frontend 파일 바로 밑에 .env.local 파일 생성

```jsx
VUE_APP_SERVER_URL=http://localhost:8000
VUE_APP_KAKAO_KEY=676c5fa31785f08e2ce866bd98c4c645
VUE_APP_FIREBASE_KEY=AIzaSyCdt9tGJ2WmiNqE5awIY0h0Jnh0YlY6o_Y
VUE_APP_FIREBASE_DOMAIN=plantit-6f6b0.firebaseapp.com
VUE_APP_FIREBASE_PROJECTID=plantit-6f6b0
VUE_APP_FIREBASE_STORAGEBUCKET=plantit-6f6b0.appspot.com
VUE_APP_FIREBASE_SENDERID=859791470292
VUE_APP_FIREBASE_APPID=1:859791470292:web:3e9efedfd45a6999a21541
VUE_APP_FIREBASE_MEASUREMENTID=G-RGSCSYPPJY
```

- npm install
- npm run serve

###### Install 오류가 발생했을 경우

- 우선 node_modules 파일과 package-lock.json 파일을 지운뒤 다시 npm install
- 해결이 안될 경우 읽기 전용 파일로 생성된 것일 수 있으니 npm install --force



------



##### 6. Backend 실행방법 및 유의사항



1. 가상환경에서 작업

   ```bash
   $ python -m venv venv
   $ source venv/Scripts/activate
   ```

2. `requirements.txt`에 적어 놓은 라이브러리 설치 👉 **cryptography 에러 발생시** `python -m pip install --upgrade pip`

   ```bash
   $ pip install -r requirements.txt
   ```

3. 서버 실행

   ```bash
   $ python manage.py runserver
   ```



------



##### 7. Server 실행방법 및 유의사항



###### *SSH & mysql(Docker)*



###### -- Docker 및 Mysql 설치

###### Docker 설치

https://soyoung-new-challenge.tistory.com/52

###### Mysql 설치

http://jmlim.github.io/docker/2019/07/30/docker-mysql-setup/

1. MYSQL Docker 이미지 다운로드

   ```
   docker pull mysql
   ```

2. docker 이미지 확인

   ```
   docker images
   ```

3. docker MYSQL 컨테이너 생성 및 실행

   ```
   docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root --name plantitDBContainer(컨테이너이름) -v /Users/multicampus/datadir:/var/lib/mysql mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
   ```

4. mysql 접속

   ```
   docker exec -it plantitDBContainer bash
   mysql -u 유저명 -p 패스워드
   ```

5. 유저생성 및 권한부여

   ```
   CREATE USER 'a101'@'%' IDENTIFIED BY '[카톡에 보낸 패스워드]';
   GRANT ALL PRIVILEGES ON *.* TO 'a101'@'%';
   flush privileges;
   ```

- mysql 있는 컨테이너 이름 : plantitDBContainer
  - mysql 계정
    - root/ root
    - a101 / [패스워드는 카톡에 보냈습니다]
- 컨테이너 bash shell 접속
  - `docker exec -it plantitDBContainer(컨테이너이름) bash`





###### Deploy

![Untitled](https://user-images.githubusercontent.com/26132746/113855421-f42a2700-97da-11eb-8577-2eef82e3a22f.png)

- docker-compose.yml 작성해준다.

```docker
# docker-compose.yml

version: '3'

services:
  vuejs:
    container_name: vuejs
    build: ./frontend
    image: frontend/vuejs
    restart: always
    ports:
      - '80:80'
    depends_on:
      - django

  django:
    container_name: django
    build: ./backend
    image: backend/django
    restart: always
    ports:
      - '8000:8000'
```

- 도커 컴포즈 올리기 (**명령어 한 줄로 배포하기**)

```bash
docker-compose up -d --build
```

- 도커 컴포즈 기본적인 명령어

```bash
docker-compose down # 도커 컴포즈 내리기
docker-compose ps # # 현재 실행 중인 도커 컴포즈 보기
```



###### Dockerizing

![Untitled (1)](https://user-images.githubusercontent.com/26132746/113855538-1de34e00-97db-11eb-9ca8-c2009dfa11a6.png)

- local version에서 수정 사항

```
front & back 카카오 도메인 수정
env 파일 도메일 수정 8000포트
```

- 기본적인 도커 명령어

```bash
docker ps   # 현재 실행 중인 컨테이너 보기 
docker stop {컨테이너 이름}    # 해당 실행 중인 컨테이너 중지  
docker images    # 도커 이미지 보기
docker image rm --force {이미지 id}    # 해당 도커 이미지 삭제
```



###### -- Backend Dockerizing



- Dockerfile을 작성해준다.

```docker
FROM python:3.7.7

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/docker
ADD . /srv/docker

WORKDIR /srv/docker

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

EXPOSE 8000 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

- 해당 프로젝트 도커화하기

```bash
docker build -t {이미지 이름} .
```

- 도커 이미지 컨테이너로 실행 (-d : daemon 버전으로 돌리기 -p : 포트 매칭해주기)

```bash
docker run -d -p 8000:8000 {이미지 이름}
```



###### -- Frontend Dockerizing



- Dockerfile을 작성해준다.

```docker
#STEP 1 BUILD VUE PROJECT 

FROM node:12.18.1-alpine AS build 
WORKDIR /app 
COPY package.json ./ 
RUN npm install 
COPY . . 
RUN npm run build

#STEP 2 CREATE NGINX SERVER 

FROM nginx:1.19.0-alpine As prod-stage 
COPY --from=build /app/dist /usr/share/nginx/html 
COPY default.conf /temp/default.conf
RUN envsubst /app < /temp/default.conf > /etc/nginx/conf.d/default.conf

EXPOSE 80 
CMD ["nginx","-g","daemon off;"]
```

- default.conf을 작성해준다.

```docker
server {
  listen 80;
  server_name _ default_server;

  root /usr/share/nginx/html;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

- 해당 프로젝트 도커화하기 (-d : daemon 버전으로 돌리기 -p : 포트 매칭해주기)

```bash
docker build -t {이미지 이름} .
```

- 도커 이미지 컨테이너로 실행

```bash
docker run -d -p 80:80 {이미지 이름}
```



------
