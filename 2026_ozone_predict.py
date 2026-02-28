import streamlit as st
import pandas as pd 
import joblib
from datetime import datetime

model = joblib.load('ozone_model_20260228_1452.joblib')

hour = datetime.now().hour
month = datetime.now().month
if month in [3, 4, 5]:
    season = 1
elif month in [6, 7, 8]:
    season = 2
elif month in [9, 10, 11]:
    season = 3
else:
    season = 4

st.title('明日臭氧濃度預測')
input_data = { 
    "氣溫(℃)" : st.number_input("請輸入現在的溫度(℃)"),
    "季節" : season,
    "Hour" : hour,
    "相對濕度( %)" : st.number_input("請輸入現在的溼度(%)")
} 
input_df = pd.DataFrame([input_data])

if st.button('顯示預測結果'):
    prediction = model.predict(input_df)
    if prediction[0]<=54:
        st.write('預測結果:', f":green[{prediction[0]}ppb,空氣品質良好]")
    elif prediction[0]<=124:
        st.write('預測結果:', f":yellow[{prediction[0]}ppb,空氣品質普通]")
    elif prediction[0]<=204:
        st.write('預測結果:', f":orange[{prediction[0]}ppb,對敏感族群不健康]")
    else:
        st.write('預測結果:', f":red[{prediction[0]}ppb,對所有族群不健康]")
    
