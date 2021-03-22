# -*- coding: utf-8 -*-
"""컨텐츠 기반 필터링 – 플랜잇 Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bZhdUWoAvH0WrHuuGQfw2QzKGCEQvrJl

### 컨텐츠 기반 필터링 – 플랜잇 Dataset
"""

import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
from google.colab import drive
drive.mount('/gdrive')

plants=pd.read_excel('/gdrive/My Drive/Colab Notebooks/DataHandling/total_plants_property_final_final_0315.xlsx')
print(plants.shape)
plants.head(10)

from sklearn.feature_extraction.text import CountVectorizer

# CountVectorizer를 적용하기 위해 공백문자로 word 단위가 구분되는 문자열로 변환. 
count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
prefer_mat = count_vect.fit_transform(plants['preference'])
print(prefer_mat.shape)

from sklearn.metrics.pairwise import cosine_similarity

prefer_sim = cosine_similarity(prefer_mat, prefer_mat)
print(prefer_sim.shape)
print(prefer_sim)

# heat_data = pd.DataFrame(prefer_sim)
# xlxs_dir = '/gdrive/My Drive/Colab Notebooks/DataHandling/heatmap.xlsx'

# with pd.ExcelWriter(xlxs_dir) as writer:
#      heat_data.to_excel(writer, sheet_name = 'heat')

prefer_sim_sorted_ind = prefer_sim.argsort()[:, ::-1]
print(prefer_sim_sorted_ind)

def find_sim_plant(df, sorted_ind, mbti_name):
    
    # 인자로 입력된 plants DataFrame에서 'plant_name' 컬럼이 입력된 mbti_name 값인 DataFrame추출
    mbti = df[df['plant_name'] == mbti_name]
    
    # mbti_name을 가진 DataFrame의 index 객체를 ndarray로 반환하고 
    # sorted_ind 인자로 입력된 prefer_sim_sorted_ind 객체에서 유사도 순으로 top_n 개의 index 추출
    mbti_index = mbti.index.values
    #similar_indexes = sorted_ind[mbti_index, :(top_n)]
    similar_indexes = sorted_ind[mbti_index]
    
    # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임. 
    #dataframe에서 index로 사용하기 위해서 1차원 array로 변경
    # print(similar_indexes)
    similar_indexes = similar_indexes.reshape(-1)
    
    return df.iloc[similar_indexes]

similar_plants = find_sim_plant(plants, prefer_sim_sorted_ind, 'ESFJ')
similar_plants = similar_plants[similar_plants['section'] == 'plant']
similar_plants[:10]

import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = [10, 8]

hm_mbti = pd.read_excel('/gdrive/My Drive/Colab Notebooks/DataHandling/heatmap_mbti_touch.xlsx')
df_mbti = hm_mbti.pivot('Comparison_MBTI', 'Type', 'Weight')
df_mbti.head()

#heatmap by plt.pcolor()
plt.pcolor(df_mbti)
plt.xticks(np.arange(0.5, len(df_mbti.columns), 1), df_mbti.columns)
plt.yticks(np.arange(0.5, len(df_mbti.index), 1), df_mbti.index)
plt.title('Heatmap by MBTI with Plantit', fontsize=20)
plt.xlabel('Type', fontsize=14)
plt.ylabel('Comparison_MBTI', fontsize=14)
plt.colorbar()
plt.show()

# different colormap
sns.heatmap(df_mbti, cmap='RdYlGn_r', annot=True, fmt='0.1f') 
plt.title('Heatmap by MBTI with Plantit', fontsize=20)
plt.show()

hm_plant = pd.read_excel('/gdrive/My Drive/Colab Notebooks/DataHandling/heatmap_plant_touch.xlsx')
df_plant = hm_plant.pivot('Comparison_Plant', 'Plant_name', 'Weight')
df_plant.head()

#heatmap by plt.pcolor()
plt.rcParams['figure.figsize'] = [10, 10]
plt.pcolor(df_plant)
plt.xticks(np.arange(0.5, len(df_plant.columns), 1), df_plant.columns)
plt.yticks(np.arange(0.5, len(df_plant.index), 1), df_plant.index)
plt.title('Heatmap by Plants with Plantit', fontsize=20)
plt.xlabel('Plant_name', fontsize=14)
plt.ylabel('Comparison_Plant', fontsize=14)
plt.colorbar()
plt.show()

hm_final = pd.read_excel('/gdrive/My Drive/Colab Notebooks/DataHandling/Drive_Final_heatmap_plant_MBTI.xlsx')
df_final = hm_final.pivot('Plant', 'MBTI', 'Weight')
df_final.head()

# different colormap
sns.heatmap(df_final, cmap='YlGnBu',annot=True, fmt='0.2f') 
plt.title('Heatmap with Plant\'it', fontsize=20)
plt.show()