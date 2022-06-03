import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

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
elif platform.system() == 'Linux':
    rc('font', family='NanumGothic')    
else:
    print('Unknown system')
############### 그래프에서 한국어 인식 ###############

def run_eda():
    st.subheader('EDA: 데이터 분석')

    st.info('기상통계와 교통통계를 아래의 체크박스를 눌러 확인할 수 있습니다.')
    st.text("")

    ### 데이터 삽입 ###
    df = pd.read_csv('data/car_accident_2016_2020.csv',index_col=0)

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
            st.text('선택한 컬럼들의 상관계수입니다.')

            if select_corr == radio_corr[0]:
                fig = sb.pairplot(data = df[selected_list])
                st.pyplot(fig)
                
            if select_corr == radio_corr[1]:
                st.dataframe(df_choice.corr())
                
            if select_corr == radio_corr[2]:
                fig2 = plt.figure()
                sb.heatmap(data= df[selected_list].corr(),annot=True,fmt='.2f', vmin=-1, vmax=1, cmap='coolwarm',linewidths= 0.5)
                st.pyplot(fig2)
                
            st.warning('위쪽의 상관관계 확인 체크박스를 풀어서 상관관계 표를 해제할수 있습니다.')
            st.write("""***""")



    # 라디오 버튼을 이용하여 데이터프레임과 통계치를 선택해서 볼수있게 한다.
    if st.checkbox('데이터프레임과 차트 생성'):
        st.text('')

        radio_menu = ['데이터프레임','통계치']
        selected = st.radio('보고 싶은 데이터프레임을 선택하세요.', radio_menu)

        if selected == radio_menu[0]:
            
            region_list = ['전체' , '강원' , '경기' , '경남' , '경북' , '광주' , '대구' , '대전' , '부산' , '서울' , '울산' , '인천' , '전남' , '전북' , '제주' , '충남' , '충북']
            get_region = st.selectbox('지역을 선택하여 데이터를 검색합니다.',region_list)
            year_list = ['전체','2020','2019','2018','2017','2016']
            get_year = st.selectbox('해당 연도의 데이터를 검색합니다.',year_list) 

            # 전체 행을 나타내기 위한 사전작업
            if get_region == region_list[0]:
                get_region = '|'.join(region_list[1:])
            if get_year == year_list[0]:
                get_year = '|'.join(year_list[1:])

            region_txt = get_region
            year_txt = get_year
            if region_txt == '|'.join(region_list[1:]):
                region_txt = '전체'            
            if year_txt == '|'.join(year_list[1:]):
                year_txt = '전체'

            # 데이터프레임과 차트 나타내기
            selected_df = df.loc[(df['date'].str.contains(get_year))&(df['시도별'].str.contains(get_region)),]
            st.dataframe(selected_df)
            selected_col_for_chart = st.selectbox('차트를 생성하기 원하면 컬럼을 선택하세요',col_list)
            if st.button('차트확인'):
                fig = plt.figure()

                if selected_col_for_chart in col_list[4:9]:                    
                    st.info('{}년도 {}지역 {}의 합을 나타낸 차트입니다.'.format(year_txt,region_txt,selected_col_for_chart))
                    x = selected_df.groupby('date')[[selected_col_for_chart]].sum().index
                    y = selected_df.groupby('date')[[selected_col_for_chart]].sum()
                
                else:
                    st.info('{}년도 {}지역 {}의 평균변화량을 나타낸 차트입니다.'.format(year_txt,region_txt,selected_col_for_chart))
                    x = selected_df.groupby('date')[[selected_col_for_chart]].mean().index
                    y = selected_df.groupby('date')[[selected_col_for_chart]].mean()

                plt.xlabel('Date')
                plt.ylabel(selected_col_for_chart)
                if year_txt == '전체':
                    plt.xticks(rotation = 45, fontsize=4 )
                else:
                    plt.xticks(rotation = 45)
                plt.plot(x,y)
                st.pyplot(fig)

        if selected == radio_menu[1]:
            st.dataframe(df.describe())
    st.write("""***""")
    if st.button('데이터 분석 의견'):
        st.info('기상통계를 보시면 평균 기온과 상대습도가 점차적으로 올라가는 경향을 보입니다.\n\n이는 대한민국의 기후가 아열대 기후로 변한다는 사실을 뒷받침하고 있습니다.\n\n다음으로 교통통계와 인구통계를 보면 사고건수와 사망자수, 그리고 부상자수가 전체적으로 줄어드는 모습을 볼수 있습니다.\n\n하지만 이를 긍정적인 결과로만으로 볼수 없습니다.\n\n그 이유는 전체적인 인구수도 함께 줄어들고 있기 때문입니다.\n\n따라서 대한민국은 아열대기후로 변하는 기상현상과 계속해서 줄어드는 인구수에 대한 대책 마련이 시급합니다.')


            ##### 첫번째 시도: streamlit의 group_by 오류  [생각해보니 st.dataframe을 변수로 지정함..]
            # selected_list_for_chart = st.selectbox('차트를 생성하기 원하면 컬럼을 선택하세요',col_list)
            # if len(selected_list_for_chart) != 0:
            #     if st.button('차트확인'):
            #         st.text('{}년도 {}지역의 {} 변화량을 나타낸 차트입니다.'.format(get_year,get_region,selected_list_for_chart))
            #         fig = plt.figure()
            #         x = df_for_chart.groupby('date')[[selected_list_for_chart]].mean().index
            #         y = df_for_chart.groupby('date')[[selected_list_for_chart]].mean()
            #         plt.xlabel('date')
            #         plt.ylabel(selected_list_for_chart)
            #         plt.xticks(rotation = 45, fontsize=4 )
            #         plt.plot(x,y)
            #         st.pyplot(fig)


            ##### 두번째 시도: 코드가 너무 길어짐
            # # 전체 지역, 전체 연도
            # if get_region == '전체' and get_year == '전체':
            #     st.dataframe(df.sort_values(['date','시도별']))
            #     selected_list_for_chart = st.selectbox('차트를 생성하기 원하면 컬럼을 선택하세요',col_list)
            #     if selected_list_for_chart in col_list[4:9]:
            #         if st.button('차트확인'):
            #             st.info('{}년도 {}지역 {}의 합을 나타낸 차트입니다.'.format(get_year,get_region,selected_list_for_chart))
            #             fig = plt.figure()
            #             x = df.groupby('date')[[selected_list_for_chart]].sum().index
            #             y = df.groupby('date')[[selected_list_for_chart]].sum()
            #             plt.xlabel('Date')
            #             plt.ylabel(selected_list_for_chart)
            #             plt.xticks(rotation = 45, fontsize=4 )
            #             plt.plot(x,y)
            #             st.pyplot(fig)

            #     else:
            #        
            #         if st.button('차트확인'):
            #             st.info('{}년도 {}지역 {}의 평균변화량을 나타낸 차트입니다.'.format(get_year,get_region,selected_list_for_chart))
            #             fig = plt.figure()
            #             x = df.groupby('date')[[selected_list_for_chart]].mean().index
            #             y = df.groupby('date')[[selected_list_for_chart]].mean()
            #             plt.xlabel('Date')
            #             plt.ylabel(selected_list_for_chart)
            #             plt.xticks(rotation = 45, fontsize=4 )
            #             plt.plot(x,y)
            #             st.pyplot(fig)
            #         

            # # 전체 지역, 특정 연도            
            # elif get_region == region_list[0]:
            #     st.dataframe(df.loc[df['date'].str.contains(get_year),])
            #     selected_list_for_chart = st.selectbox('차트를 생성하기 원하면 컬럼을 선택하세요',col_list)
            #     if selected_list_for_chart in col_list[4:9]:
            #         if st.button('차트확인'):
            #             st.info('{}년도 {}지역 {}의 합을 나타낸 차트입니다.'.format(get_year,get_region,selected_list_for_chart))
            #             fig = plt.figure()
            #             x = df.loc[df['date'].str.contains(get_year),].groupby('date')[[selected_list_for_chart]].sum().index
            #             y = df.loc[df['date'].str.contains(get_year),].groupby('date')[[selected_list_for_chart]].sum()
            #             plt.xlabel('Date')
            #             plt.ylabel(selected_list_for_chart)
            #             plt.xticks(rotation = 45 )
            #             plt.plot(x,y)
            #             st.pyplot(fig)

            #     else:
            # 
            #         if st.button('차트확인'):
            #             st.info('{}년도 {}지역 {}의 평균변화량을 나타낸 차트입니다.'.format(get_year,get_region,selected_list_for_chart))
            #             fig = plt.figure()
            #             x = df.loc[df['date'].str.contains(get_year),].groupby('date')[[selected_list_for_chart]].mean().index
            #             y = df.loc[df['date'].str.contains(get_year),].groupby('date')[[selected_list_for_chart]].mean()
            #             plt.xlabel('Date')
            #             plt.ylabel(selected_list_for_chart)
            #             plt.xticks(rotation = 45 )
            #             plt.plot(x,y)
            #             st.pyplot(fig)
            #     

            # # 특정 지역, 전체 연도  
            # elif get_year == year_list[0]:
            #     st.dataframe(df.loc[df['시도별'].str.contains(get_region),])
            #     selected_list_for_chart = st.selectbox('차트를 생성하기 원하면 컬럼을 선택하세요',col_list)
            #     if len(selected_list_for_chart) != 0:
            #     # if selected_list_for_chart in col_list[4:9]:
            #         if st.button('차트확인'):
            #             st.info('{}년도 {}지역 {}의 차트입니다.'.format(get_year,get_region,selected_list_for_chart))
            #             fig = plt.figure()
            #             x = df.loc[df['시도별'].str.contains(get_region),]['date']
            #             y = df.loc[df['시도별'].str.contains(get_region),][selected_list_for_chart]
            #             plt.xlabel('Date')
            #             plt.ylabel(selected_list_for_chart)
            #             plt.xticks(rotation = 45, fontsize=4)
            #             plt.plot(x,y)
            #             st.pyplot(fig)


            # # 특정 지역, 특정 연도  
            # else:
            #     st.dataframe(df.loc[(df['date'].str.contains(get_year))&(df['시도별'].str.contains(get_region)),])
            #     selected_list_for_chart = st.selectbox('차트를 생성하기 원하면 컬럼을 선택하세요',col_list)
            #     if len(selected_list_for_chart) != 0:

            #       
            #         if st.button('차트확인'):
            #             st.info('{}년도 {}지역 {}의 차트입니다.'.format(get_year,get_region,selected_list_for_chart))
            #             fig = plt.figure()
            #             x = df.loc[(df['date'].str.contains(get_year))&(df['시도별'].str.contains(get_region)),]['date']
            #             y = df.loc[(df['date'].str.contains(get_year))&(df['시도별'].str.contains(get_region)),][selected_list_for_chart]
            #             plt.xlabel('Date')
            #             plt.ylabel(selected_list_for_chart)
            #             plt.xticks(rotation = 45 )
            #             plt.plot(x,y)
            #             st.pyplot(fig)
            #    