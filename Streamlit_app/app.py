# input field haru yehhaa banauchham.
import streamlit as st
st.set_page_config(
    page_title = 'Diabets Prediction APP'
)

st.title ('Diabetes Prediction')
st.header('Input your data:')

glucose = st.number_input('Glucose', min_value =0 , max_value = 400 , value =20)# value = something bhaneko tehaa display kati huney?
BloodPressure = st.number_input('BloodPressure', 0,200,0)