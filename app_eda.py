import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from datetime import datetime, date

############### 그래프에서 한국어 인식 ###############
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system')
############### 그래프에서 한국어 인식 ###############

def run_eda():
    st.subheader('EDA: 데이터 분석')

    st.info('기상통계와 교통통계를 아래의 체크박스를 눌러 확인할 수 있습니다.')
    st.text("")

    ### 데이터 삽입 ###
    df = pd.read_csv('data/car_accident.csv',index_col=0)

     # 유저가 선택한 컬럼들만 pairplot그리고 그다음에 상관계수를 보여준다.
    col_list = df.columns[2:]
    if st.checkbox('상관관계 확인'):
        st.text('')
        selected_list = st.multiselect('상관관계를 보기 원하면, 하나 이상의 컬럼을 선택하세요',col_list)
        st.text('')
        df_choice = df[selected_list]
        radio_corr = ['그래프','표','히트맵']
        if len(selected_list) > 1:
            select_corr = st.radio('상관계수를 표시할 방법을 선택하세요.',radio_corr)
            st.text('')

            if select_corr == radio_corr[0]:

                st.text('선택한 컬럼들의 상관계수입니다.')
                fig = sb.pairplot(data = df[selected_list])
                st.pyplot(fig)

            if select_corr == radio_corr[1]:

                st.text('선택한 컬럼들의 상관계수입니다.')
                st.dataframe(df_choice.corr())
            
            if select_corr == radio_corr[2]:

                st.text('선택한 컬럼들의 상관계수입니다.')
                fig2 = plt.figure()
                sb.heatmap(data= df[selected_list].corr(),annot=True,fmt='.2f', vmin=-1, vmax=1, cmap='coolwarm',linewidths= 0.5)
                st.pyplot(fig2)



    # 라디오 버튼을 이용하여 데이터프레임과 통계치를 선택래서 볼수있게 한다.
    if st.checkbox('사용된 데이터프레임 확인'):
        st.text('')

        radio_menu = ['데이터프레임','통계치']
        selected = st.radio('보고 싶은 데이터프레임을 선택하세요.', radio_menu)

        if selected == radio_menu[0]:
            
            region_list = ['전체','강원' , '경기' , '경남' , '경북' , '광주' , '대구' , '대전' , '부산' , '서울' , '울산' , '인천' , '전남' , '전북' , '제주' , '충남' , '충북']
            get_region = st.selectbox('지역을 선택하여 데이터를 검색합니다.',region_list)
            year_list = ['전체','2020','2019','2018','2017','2016']
            get_year = st.selectbox('해당 연도의 데이터를 검색합니다.',year_list)


            if get_region == '전체' and get_year == '전체':
                data_for_chart = st.dataframe(df.sort_values(['date','시도별']))
            elif get_region == region_list[0]:
                data_for_chart = st.dataframe(df.loc[df['date'].str.contains(get_year),])
            elif get_year == year_list[0]:
                data_for_chart = st.dataframe(df.loc[df['시도별'].str.contains(get_region),])
            else:
                data_for_chart = st.dataframe(df.loc[(df['date'].str.contains(get_year))&(df['시도별'].str.contains(get_region)),])

