# Weather_And_Car_Accident

이 앱은 교통사고 통계와 기상청의 종관기상 통계를 학습하여 날씨를 입력받으면 교통사고율을 예측할수 있는 앱입니다.

메뉴는 Home, EDA, ML로 구성되어 있습니다:

Home: 이 앱의 사용목적과 사용된 데이터를 나타내었습니다.
EDA: 사용된 데이터를 데이터프레임 등으로 나타내고 한눈에 보기쉽게 차트를 보여줍니다.
ML: 학습된 인공지능을 바탕으로 사용자로 부터 날씨데이터를 수집하여 사고율을 예측합니다.

2016년 부터 2020년까지의 대한민국의 기상상황과 교통사고 데이터를 지역과 날짜(년,월)를 기준으로 정리하여 인공지능을 학습시켰습니다. 

인공지능은 Random Forest를 사용했습니다.

*기상청에서 제공된 데이터의 날짜에 일(day) 정보가 포함되어있지 않기 때문에 정확한 측정이 불가능했습니다. 
*교통사고는 기상상황 외에 수많은 요인들이 있기 때문에 사고율과 기상상황과의 상관관계지수는 낮습니다.