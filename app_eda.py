import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda():
    st.subheader('EDA: 데이터 분석')

    st.text('기상통계와 교통통계를 확인할 수 있습니다.')
    st.text("")
    df = pd.read_csv('data/car_accident.csv',index_col=0)

    # 라디오 버튼을 이용하여 데이터프레임과 통계치를 선택래서 볼수있게 한다.
    if st.checkbox('사용된 데이터프레임 확인'):
        st.text('')

        radio_menu = ['데이터프레임','통계치']
        selected = st.radio('보고 싶은 데이터프레임을 선택하세요', radio_menu)

        if selected == radio_menu[0]:
            st.dataframe(df)

        if selected == radio_menu[1]:
            st.dataframe(df.describe())

    # 컬럼명을 보여주고 컬럼을 선택하면
    # 해당컬럼의 최대값 데이터와 최소값 데이터를 보여준다.

    col_list = df.columns[4:]

    selected_column = st.selectbox('최대값과 최소값을 보기 원하는 컬럼을 선택하세요',col_list)

    df_max = df.loc[df[selected_column] == df[selected_column].max(),]
    df_min = df.loc[df[selected_column] == df[selected_column].min(),]

    st.text('{} 컬럼의 최대값입니다'.format(selected_column))
    st.dataframe(df_max)

    st.text('{} 컬럼의 최소값입니다'.format(selected_column))
    st.dataframe(df_min)


    # 유저가 선택한 컬럼들만 pairplot그리고 그다음에 상관계수를 보여준다.
    selected_list = st.multiselect('상관관계를 보기 원하는 컬럼을 선택하세요',col_list)

    if len(selected_list) > 1:

        df_choice = df[selected_list]

        fig = sb.pairplot(data = df[selected_list])
        st.pyplot(fig)

        st.text('선택하신 컬럼들의 상관계수입니다.')
        st.dataframe(df_choice.corr())

        fig2 = plt.figure()
        sb.heatmap(data= df[selected_list].corr(),annot=True,fmt='.2f', vmin=-1, vmax=1, cmap='coolwarm',linewidths= 0.5)
        st.pyplot(fig2)

    # 고객이름 컬럼을 검색할수 있게 만듭니다
    # 검색한 글자가 포함된 이름을 가져올수있도록

    # 유저한테 검색어를 입력 받는다.
    get_date = st.text_input('날짜를 검색할수 있습니다. (YYYY-MM-01)')
    get_region = st.text_input('지역을 검색할수 있습니다. (예: 경남)')

    # 검색어를 고객이름 컬럼에 들어있는 데이터 가져온다

    result = df.loc[(df['date'].str.contains(get_date))&(df['시도별'].str.contains(get_region)),]

    if len(get_date) != 0:
        st.dataframe(result)

    # 화면에 보여준다.