import streamlit as st
import joblib
import numpy as np
import sklearn

def run_ml():
    st.subheader('자동차 구매 가능 가격 예측')
    # 예측하기위해서 필요한 파일들을 불러와야 한다.
    # 인공지능파일과 스케일러 파일 2개


    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')


# 사용자가 데이터 입력
# 얼마정도의 차를 구매할수 있는지?
# 여자, 나이 38, 연봉 78000, 카드빛 15000 자산 480000

# 성별, 나이 , 연봉, 카드빛, 자산

    gender = st.radio('성별을 고르세요', ['남자','여자'])
    if gender == '여자':
        gender = 0
    else:
        gender = 1
    age = st.number_input('나이를 입력하세요',0,120)
    salary = st.number_input('연봉을 입력하세요',0)
    debt = st.number_input('카드 빛을 입력하세요',0)
    asset = st.number_input('자산을 입력하세요',0)

    if st.button('자동차 구매 금액 예측'): 


        # 1. 신규고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([gender, age, salary, debt, asset])

        # 2. 학습할때 사용한 X의 피텨스케일링을 이용해서 피처스케일링 한다.
        # 먼저 데이터를 2차원으로 만든다. 
        new_data = new_data.reshape(1,5)
        new_data = scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        y_pred = regressor.predict(new_data)

        # 4. 예측한값을 원상복구한다.
        y_pred = scaler_y.inverse_transform(y_pred)

        st.write('이 사람의 구매 가능 금액은 '+ str(round(y_pred[0,0])) +'달러 입니다.')

