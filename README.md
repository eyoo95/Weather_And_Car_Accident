π¦οΈκΈ°μμ λ³΄λ₯Ό ν΅ν κ΅ν΅μ¬κ³ μ¨ μμΈ‘ μ±
========

μ΄ μ±μ κ΅ν΅μ¬κ³  ν΅κ³μ κΈ°μμ²­μ μ’κ΄κΈ°μ ν΅κ³λ₯Ό νμ΅νμ¬ λ μ¨λ₯Ό μλ ₯λ°μΌλ©΄ κ΅ν΅μ¬κ³ μ¨μ μμΈ‘ν μ μλ μ±μλλ€.

μ±μ£Όμ
----
http://ec2-52-79-80-210.ap-northeast-2.compute.amazonaws.com:8501/

λ©λ΄κ΅¬μ±
----
λ©λ΄λ Home, EDA, MLλ‘ κ΅¬μ±λμ΄ μμ΅λλ€:

- Home: μ΄ μ±μ μ¬μ©λͺ©μ κ³Ό μ¬μ©λ λ°μ΄ν°λ₯Ό λνλ΄μμ΅λλ€.
- EDA: μ¬μ©λ λ°μ΄ν°λ₯Ό λ°μ΄ν°νλ μ λ±μΌλ‘ λνλ΄κ³  νλμ λ³΄κΈ°μ½κ² μ°¨νΈλ₯Ό λ³΄μ¬μ€λλ€.
- ML: νμ΅λ μΈκ³΅μ§λ₯μ λ°νμΌλ‘ μ¬μ©μλ‘ λΆν° λ μ¨λ°μ΄ν°λ₯Ό μμ§νμ¬ μ¬κ³ μ¨μ μμΈ‘ν©λλ€.

μ¬μ©λ λ°μ΄ν°
----
2016λ λΆν° 2020λκΉμ§μ λνλ―Όκ΅­μ κΈ°μμν©κ³Ό κ΅ν΅μ¬κ³  λ°μ΄ν°λ₯Ό μ§μ­κ³Ό λ μ§(λ,μ)λ₯Ό κΈ°μ€μΌλ‘ μ λ¦¬νμ¬ μΈκ³΅μ§λ₯μ νμ΅μμΌ°μ΅λλ€. 

Dataset:

KOSIS (λνλ―Όκ΅­ κ΅ν΅ν΅κ³ λ° κΈ°μν΅κ³)
- [μ’κ΄κΈ°μ] μ§μ λ³ μ°Β·μ ν΅κ³
- μγ»λλ³ λλ‘λ³΄κΈλ₯ 
- μλλ³ κ΅ν΅μ¬κ³ 
- λλ‘κ΅ν΅μ¬κ³  μ¬λ§λ₯ 
>https://kosis.kr/statHtml/statHtml.do?orgId=132&tblId=DT_V_MOTA_016

μ¬μ©λ μ»¬λΌ
----
- μλλ³: λνλ―Όκ΅­μ μλλ₯Ό λνλ΄μμ΅λλ€. μΈλΆνλ μ§μ­μ νλμ μλμ μΆκ°νμΌλ©° μΈμ’μ§μ­μ΄ μλ λ°μ΄ν°κ° μκΈ°μ μΈμ’μ§μ­μ μ κ±°νμ΅λλ€. 
- date: λ μ§λ₯Ό λ,μ,μΌλ‘ λνλλλ€. μ€μ λ‘λ raw λ°μ΄ν°μ μΌ λ¨μκ° μκΈ° λλ¬Έμ μλ³λ‘ 1μΌμ λ£μμ΅λλ€. 
- βμ΅λνμ(m/s): μ΅λνμμ m/sλ¨μλ‘ λνλλλ€.
- βνκ· κΈ°μ¨(β): νκ· κΈ°μ¨μ β λ¨μλ‘ λνλλλ€.
- βνκ· κ°μλ(mm): νκ· κ°μλμ mm λ¨μλ‘ λνλλλ€.
- βνκ· μλμ΅λ(%):νκ· μλμ΅λλ₯Ό % λ¨μλ‘ λνλλλ€.
- μ¬κ³ κ±΄μ: λλλ³, μ§μ­λ³λ‘ κ΅ν΅μ¬κ³  κ±΄μλ₯Ό λ³΄μ¬μ€λλ€.
- μ¬λ§μμ: λλλ³, μ§μ­λ³λ‘ κ΅ν΅μ¬κ³ μ μν μ¬λ§μμλ₯Ό λ³΄μ¬μ€λλ€.
- λΆμμμ: λλλ³, μ§μ­λ³λ‘ κ΅ν΅μ¬κ³ μ μν λΆμμμλ₯Ό λ³΄μ¬μ€λλ€.
- μλλ³μΈκ΅¬μ: λλλ³, μ§μ­λ³λ‘ μΈκ΅¬μλ₯Ό λ³΄μ¬μ€λλ€.
- μλμ°¨μ: λλλ³, μ§μ­λ³λ‘ μλμ°¨μλ₯Ό λ³΄μ¬μ€λλ€.
- κ΅ν΅μ¬κ³ μ¬λ§λ₯ : (μ¬λ§μμ Γ· μ΄μΈκ΅¬) Γ 100,000λ‘ κ³μ°νμ΅λλ€. 
- βμ¬κ³ μ¨: μ¬λ§μμ Γ· μ¬κ³ κ±΄μλ‘ κ³μ°νμ΅λλ€. 

μΈκ³΅μ§λ₯ νμ΅μ μ¬μ©λ μ»¬λΌμ βνμλ₯Ό νμ΅λλ€.

μ¬μ©λ λΌμ΄λΈλ¬λ¦¬
----
- streamlit
``` python
pip install streamlit
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

*μΈκ³΅μ§λ₯μ Random Forestλ₯Ό μ¬μ©νμ΅λλ€.
>MSE(Mean Squared Error): 0.7136217880179686

----

*κΈ°μμ²­μμ μ κ³΅λ λ°μ΄ν°μ λ μ§μ μΌ(day) μ λ³΄κ° ν¬ν¨λμ΄μμ§ μκΈ° λλ¬Έμ μ νν μΈ‘μ μ΄ λΆκ°λ₯νμ΅λλ€. 

*κ΅ν΅μ¬κ³ λ κΈ°μμν© μΈμ μλ§μ μμΈλ€μ΄ μκΈ° λλ¬Έμ μ¬κ³ μ¨κ³Ό κΈ°μμν©κ³Όμ μκ΄κ΄κ³μ§μλ λ?μ΅λλ€.

*λλ‘κ΅ν΅μ¬κ³ μ¬λ§λ₯  μμμΆμ²:
>https://www.index.go.kr/unify/idx-info.do?idxCd=4261
