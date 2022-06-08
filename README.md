🌦️기상정보를 통한 교통사고율 예측 앱
========

이 앱은 교통사고 통계와 기상청의 종관기상 통계를 학습하여 날씨를 입력받으면 교통사고율을 예측할수 있는 앱입니다.

앱주소
----
http://ec2-52-79-80-210.ap-northeast-2.compute.amazonaws.com:8501/

메뉴구성
----
메뉴는 Home, EDA, ML로 구성되어 있습니다:

- Home: 이 앱의 사용목적과 사용된 데이터를 나타내었습니다.
- EDA: 사용된 데이터를 데이터프레임 등으로 나타내고 한눈에 보기쉽게 차트를 보여줍니다.
- ML: 학습된 인공지능을 바탕으로 사용자로 부터 날씨데이터를 수집하여 사고율을 예측합니다.

사용된 데이터
----
2016년 부터 2020년까지의 대한민국의 기상상황과 교통사고 데이터를 지역과 날짜(년,월)를 기준으로 정리하여 인공지능을 학습시켰습니다. 

Dataset:

KOSIS (대한민국 교통통계 및 기상통계)
- [종관기상] 지점별 연·월 통계
- 시・도별 도로보급률
- 시도별 교통사고
- 도로교통사고 사망률
>https://kosis.kr/statHtml/statHtml.do?orgId=132&tblId=DT_V_MOTA_016

사용된 컬럼
----
- 시도별: 대한민국의 시도를 나타내었습니다. 세분화된 지역은 하나의 시도에 추가했으며 세종지역이 없는 데이터가 있기에 세종지역은 제거했습니다. 
- date: 날짜를 년,월,일로 나타냅니다. 실제로는 raw 데이터에 일 단위가 없기 때문에 월별로 1일을 넣었습니다. 
- ✔최대풍속(m/s): 최대풍속을 m/s단위로 나타냅니다.
- ✔평균기온(℃): 평균기온을 ℃ 단위로 나타냅니다.
- ✔평균강수량(mm): 평균강수량을 mm 단위로 나타냅니다.
- ✔평균상대습도(%):평균상대습도를 % 단위로 나타냅니다.
- 사고건수: 년도별, 지역별로 교통사고 건수를 보여줍니다.
- 사망자수: 년도별, 지역별로 교통사고에 의한 사망자수를 보여줍니다.
- 부상자수: 년도별, 지역별로 교통사고에 의한 부상자수를 보여줍니다.
- 시도별인구수: 년도별, 지역별로 인구수를 보여줍니다.
- 자동차수: 년도별, 지역별로 자동차수를 보여줍니다.
- 교통사고사망률: (사망자수 ÷ 총인구) × 100,000로 계산했습니다. 
- ✔사고율: 사망자수 ÷ 사고건수로 계산했습니다. 

인공지능 학습에 사용된 컬럼에 ✔표시를 했습니다.

사용된 라이브러리
----
- streamlit
``` python
pip install streamlit
streamlit hello
```
- streamlit_option_menu
``` python
pip install streamlit_option_menu
```
- pandas
``` python
pip install streamlit_option_menu
```
- seaborn
``` python
pip install seaborn
```
- matplotlib
``` python
pip install matplotlib
```
- joblib
``` python
pip install joblib
```
- numpy
``` python
pip install numpy
```

*인공지능은 Random Forest를 사용했습니다.
>MSE(Mean Squared Error): 0.7136217880179686

----

*기상청에서 제공된 데이터의 날짜에 일(day) 정보가 포함되어있지 않기 때문에 정확한 측정이 불가능했습니다. 

*교통사고는 기상상황 외에 수많은 요인들이 있기 때문에 사고율과 기상상황과의 상관관계지수는 낮습니다.

*도로교통사고사망률 수식출처:
>https://www.index.go.kr/unify/idx-info.do?idxCd=4261
