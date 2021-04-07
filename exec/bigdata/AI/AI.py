from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import pandas as pd
import random
#data 쪼개기
from sklearn.model_selection import train_test_split
#pickle로 저장
import pickle
import joblib
#정확도 측정
from sklearn.metrics import accuracy_score


#data 불러오기
#datas = pd.read_excel("C:/Users/multicampus/Desktop/Backend_Plant_Recommend_System/data_mbti.xlsx", engine = 'openpyxl')
datas = pd.read_excel("C:/Users/multicampus/Desktop/ssafy2/data/data.xlsx", engine = 'openpyxl')
values = datas.sample(frac=1).values

input_data = []
output_data = []

#"모른다"를 제외하고 input(대답 항목)과 output(MBTI)로 분류해서 append
for v in values:
    if "모른다" in v[9]:
        continue
    input_data.append(v[1:9])
    output_data.append(v[9])

pre_output = []
#우리가 예측한 값과 비교
for i in input_data:
    out = ""
    if i[0] + i[1] >= 5:
        out += "E"
    else:
        out += "I"
        
    if i[2] + i[3] >= 5:
        out += "N"
    else:
        out += "S"
        
    if i[4] + i[5] >= 5:
        out += "F"
    else:
        out += "T"
        
    if i[6] + i[7] >= 5:
        out += "P"
    else:
        out += "J"

    pre_output.append(out)
    
cnt_t = 0
cnt_f = 0
for i in range(0, len(pre_output)):
    if pre_output[i] == output_data[i]:
        cnt_t += 1
    else:
        cnt_f += 1

print("예측과 맞은 값 : "+ str(cnt_t) +", 예측과 틀린 값 : " + str(cnt_f))

auto_input_data = []
auto_output_data = []
num_of_auto = 86 #임의로 만들 숫자

while "ISTP" not in auto_output_data or "ESTP" not in auto_output_data:
    for i in range(0, num_of_auto):
        temp = []
        for i in range(0, 8):
            temp.append(random.randrange(1,5))

        auto_input_data.append(temp)

        out = ""
        if temp[0] + temp[1] >= 5:
            out += "E"
        else:
            out += "I"

        if temp[2] + temp[3] >= 5:
            out += "N"
        else:
            out += "S"

        if temp[4] + temp[5] >= 5:
            out += "F"
        else:
            out += "T"

        if temp[6] + temp[7] >= 5:
            out += "P"
        else:
            out += "J"

        auto_output_data.append(out)
    
input_data = input_data * 5
output_data = output_data * 5

print(len(input_data))

input_data += auto_input_data
output_data += auto_output_data

train_input, test_input, train_output, test_output = train_test_split(input_data, output_data, test_size=0.20, random_state=1)

#학습
# ppn = Perceptron(eta0=0.01, random_state=1)
# ppn.fit(train_input, train_output)

# lr = LogisticRegression(C=0.1, random_state=1)
# lr.fit(train_input, train_output)

svm = SVC(kernel='rbf', random_state=1, gamma=0.1, C=10)
svm.fit(train_input, train_output)

saved_model = pickle.dumps(svm)
joblib.dump(svm, 'mbti.pkl') 

#결과
# y_pred_ppn = ppn.predict(test_input)
# y_pred_lr = lr.predict(test_input)
y_pred_svm = svm.predict(test_input)

#성공율 추출
# print('Accuracy: %.4f' % accuracy_score(test_output, y_pred_ppn))
# print('Accuracy: %.4f' % accuracy_score(test_output, y_pred_lr))
print('Accuracy: %.4f' % accuracy_score(test_output, y_pred_svm))
