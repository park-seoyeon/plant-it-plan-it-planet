import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import requests
import json
import jwt
import pymysql
from django.http import JsonResponse
from rest_framework.decorators import api_view
from backend.settings import conn
from backend.my_settings import JWT_SECRET_KEY, JWT_ALGORITHM, KAKAO_API_KEY
from survey.models.survey import Survey

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


curs = conn.cursor(pymysql.cursors.DictCursor)

# mbti 검사 결과 보내주기


@api_view(['POST'])
def getSurveyAnswer(request):

    answer_list = []
    data = json.loads(request.body)
    answer_list = data['answer_list']

    # mbti결과 가져오기
    mbti_from_joblib = joblib.load('./survey/svm_weight/mbti.pkl')
    mbti_output = mbti_from_joblib.predict([answer_list[0:8]])[0]

    # mbti 결과별로 설문결과페이지 뿌리기
    mbti_list = []
    sql = "select * from mbti where mbti_name = %s"
    curs.execute(sql, mbti_output)
    mbti_list = curs.fetchall()

    # 궁합 가져오기
    compatibility_list = []
    sql = "select * from mbti_compatibility where mbti_name = %s"
    curs.execute(sql, mbti_output)
    compatibility_list = curs.fetchall()

    # 식물 추천 해주기
    plants_list = []
    sql = "select * from mbti_environment_recommend"
    curs.execute(sql)
    plants_list = curs.fetchall()
    plant_df = pd.DataFrame(plants_list)

    count_vect = CountVectorizer(min_df=0, ngram_range=(1, 2))
    prefer_mat = count_vect.fit_transform(plant_df['preference'])
    prefer_sim = cosine_similarity(prefer_mat, prefer_mat)
    prefer_sim_sorted_ind = prefer_sim.argsort()[:, ::-1]

    similar_plants = find_sim_plant(
        plant_df, prefer_sim_sorted_ind, mbti_output)

    # 질문지에서 가져오는 값으로 변수 바꾸기

    # 외관상 추천받은 식물들
    prefer_plants = similar_plants[similar_plants['section'] == 'plant']

    # 주거환경에 따라 추천받은 식물들
    if answer_list[9] == 1 or answer_list[9] == 2:
        answer_list[9] = 1
    else:
        answer_list[9] = 0

    if answer_list[11] == 1:
        answer_list[11] = 0
    else:
        answer_list[11] = 1

    similar_plants = similar_plants[similar_plants['section'] == 'plant']
    similar_plants = similar_plants[similar_plants['sunlight'].str.contains(
        str(answer_list[8]))]
    similar_plants = similar_plants[similar_plants['air_purification']
                                    == answer_list[9]]
    similar_plants = similar_plants[similar_plants['humidity'].str.contains(
        str(answer_list[10]))]
    similar_plants = similar_plants[similar_plants['pet_safe']
                                    == answer_list[11]]
    prefer_plants = prefer_plants[:5]
    similar_plants = pd.concat(
        [similar_plants, prefer_plants], ignore_index=True)

    # 'user_number'를 추가해야 됨
    result_json = {
        'user_number': answer_list[12],
        'mbti_name': mbti_output,
        'mbti_expression': mbti_list[0]['mbti_expression'],
        'flower_language': mbti_list[0]['flower_language'],
        'flower_description': mbti_list[0]['flower_description'],
        'best_partner': compatibility_list[0]['best_partner'],
        'best_expression': compatibility_list[0]['best_expression'],
        'worst_partner': compatibility_list[0]['worst_partner'],
        'worst_expression': compatibility_list[0]['worst_expression'],
        'recommanded_plant_1_id': int(similar_plants.iloc[0]['id']),
        'recommanded_plant_1_name': similar_plants.iloc[0]['plant_name'],
        'recommanded_plant_1_intro': similar_plants.iloc[0]['plant_intro'],
        'recommanded_plant_2_id': int(similar_plants.iloc[1]['id']),
        'recommanded_plant_2_name': similar_plants.iloc[1]['plant_name'],
        'recommanded_plant_2_intro': similar_plants.iloc[1]['plant_intro'],
        'recommanded_plant_3_id': int(similar_plants.iloc[2]['id']),
        'recommanded_plant_3_name': similar_plants.iloc[2]['plant_name'],
        'recommanded_plant_3_intro': similar_plants.iloc[2]['plant_intro'],
        'recommanded_plant_4_id': int(similar_plants.iloc[3]['id']),
        'recommanded_plant_4_name': similar_plants.iloc[3]['plant_name'],
        'recommanded_plant_4_intro': similar_plants.iloc[3]['plant_intro'],
        'recommanded_plant_5_id': int(similar_plants.iloc[4]['id']),
        'recommanded_plant_5_name': similar_plants.iloc[4]['plant_name'],
        'recommanded_plant_5_intro': similar_plants.iloc[4]['plant_intro']
    }

    sql = "select survey from user where user_number = %s"
    curs.execute(sql, answer_list[12])
    survey_done = curs.fetchall()

    if survey_done[0]['survey'] == 1:
        sql = "UPDATE user_detail SET mbti_name=%s, mbti_expression=%s, flower_language=%s, \
            best_partner = % s, best_expression = % s, worst_partner = % s, worst_expression = % s, \
            recommanded_plant_1_id = % s, recommanded_plant_1_name = % s, recommanded_plant_1_intro = % s, \
            recommanded_plant_2_id=%s, recommanded_plant_2_name = % s, recommanded_plant_2_intro = % s, \
            recommanded_plant_3_id = % s, recommanded_plant_3_name = % s, recommanded_plant_3_intro = % s, \
            recommanded_plant_4_id = % s, recommanded_plant_4_name = % s, recommanded_plant_4_intro = % s, \
            recommanded_plant_5_id=%s ,recommanded_plant_5_name=%s, recommanded_plant_5_intro=%s, flower_description=%s WHERE user_number=%s"
        curs.execute(sql, (result_json['mbti_name'], result_json['mbti_expression'], result_json['flower_language'],
                           result_json['best_partner'], result_json['best_expression'], result_json[
                               'worst_partner'], result_json['worst_expression'],
                           result_json['recommanded_plant_1_id'], result_json[
                               'recommanded_plant_1_name'], result_json['recommanded_plant_1_intro'],
                           result_json['recommanded_plant_2_id'], result_json[
                               'recommanded_plant_2_name'], result_json['recommanded_plant_2_intro'],
                           result_json['recommanded_plant_3_id'], result_json[
                               'recommanded_plant_3_name'], result_json['recommanded_plant_3_intro'],
                           result_json['recommanded_plant_4_id'], result_json[
                               'recommanded_plant_4_name'], result_json['recommanded_plant_4_intro'],
                           result_json['recommanded_plant_5_id'], result_json['recommanded_plant_5_name'], result_json['recommanded_plant_5_intro'], result_json['flower_description'], result_json['user_number']))

    else:
        sql = "UPDATE user SET survey=1 WHERE user_number=%s"
        curs.execute(sql, (answer_list[12]))
        sql = "insert into user_detail(user_number, mbti_name, mbti_expression, flower_language, best_partner, best_expression, worst_partner, \
            worst_expression, recommanded_plant_1_id, recommanded_plant_1_name, recommanded_plant_1_intro, recommanded_plant_2_id, recommanded_plant_2_name, \
            recommanded_plant_2_intro, recommanded_plant_3_id, recommanded_plant_3_name, recommanded_plant_3_intro, recommanded_plant_4_id, recommanded_plant_4_name, \
            recommanded_plant_4_intro, recommanded_plant_5_id,recommanded_plant_5_name,recommanded_plant_5_intro, flower_description) \
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        curs.execute(sql, (result_json['user_number'], result_json['mbti_name'], result_json['mbti_expression'], result_json['flower_language'],
                           result_json['best_partner'], result_json['best_expression'], result_json[
                               'worst_partner'], result_json['worst_expression'],
                           result_json['recommanded_plant_1_id'], result_json[
                               'recommanded_plant_1_name'], result_json['recommanded_plant_1_intro'],
                           result_json['recommanded_plant_2_id'], result_json[
                               'recommanded_plant_2_name'], result_json['recommanded_plant_2_intro'],
                           result_json['recommanded_plant_3_id'], result_json[
                               'recommanded_plant_3_name'], result_json['recommanded_plant_3_intro'],
                           result_json['recommanded_plant_4_id'], result_json[
                               'recommanded_plant_4_name'], result_json['recommanded_plant_4_intro'],
                           result_json['recommanded_plant_5_id'], result_json['recommanded_plant_5_name'], result_json['recommanded_plant_5_intro'], result_json['flower_description']))

    conn.commit()

    return JsonResponse({"message": "success"}, status=200)


def find_sim_plant(df, sorted_ind, mbti_name):

    # 인자로 입력된 plants DataFrame에서 'plant_name' 컬럼이 입력된 mbti_name 값인 DataFrame추출
    mbti = df[df['plant_name'] == mbti_name]

    # mbti_name을 가진 DataFrame의 index 객체를 ndarray로 반환하고
    # sorted_ind 인자로 입력된 prefer_sim_sorted_ind 객체에서 유사도 순으로 top_n 개의 index 추출
    mbti_index = mbti.index.values
    similar_indexes = sorted_ind[mbti_index]

    # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임.
    # dataframe에서 index로 사용하기 위해서 1차원 array로 변경
    similar_indexes = similar_indexes.reshape(-1)

    return df.iloc[similar_indexes]
