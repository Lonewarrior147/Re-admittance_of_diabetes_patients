import streamlit as st
import numpy as np
import pickle as pkl
from prediction import predict

pickle_in1 = open('DIA.pkl', 'rb')  
classifier1 = pickle.load(pickle_in1)  

def prediction1(race,gender,age,number_diagoneses,weight,metformin,glimepiride,glipizide,glyburide,pioglitazone,rosiglitazone,insulin,diabetesMed):  
    prediction = classifier1.predict([[race,gender,age,number_diagoneses,weight,metformin,glimepiride,glipizide,glyburide,pioglitazone,rosiglitazone,insulin,diabetesMed]])  
    return prediction
def main():
    st.title("Re-Admittance of Diabetic Patients")
    
    race = st.selectbox('Enter Race',('Caucasian','African American','Asian','Other'))
    gender = st.selectbox("Enter Gender",('Male','Female'))
    age = st.selectbox("Enter Age",('[0,10)','[10,20)','[20,30)','[30,40)','[40,50)','[50,60)','[60,70)','[70,80)','[80,90)','[90,100)'))
    number_diagoneses = st.selectbox("Enter Number of Diagoneses",('1','2','3','4','5','6','7','8','9'))
    weight = st.selectbox("Enter weight",('[0,25)','[25,50)','[50,5)','[75,100)','[100,125)','[125,150)','[150,175)','[175,200)','>200'))
    metformin = st.selectbox("State after Metformin consumption",('Steady','Up','Down','No'),key="option1")
    glimepiride = st.selectbox("State after glimepiriide consumption",('Steady','Up','Down','No'),key="option2")
    glipizide = st.selectbox("State after glipizide consumption",('Steady','Up','Down','No'),key="option3")
    glyburide = st.selectbox("State after glyburide consumption",('Steady','Up','Down','No'),key="option4")
    pioglitazone = st.selectbox("State after pioglitazone consumption",('Steady','Up','Down','No'),key="option5")
    rosiglitazone = st.selectbox("State after pioglitazone consumption",('Steady','Up','Down','No'),key="option6")
    insulin = st.selectbox("State after insulin consumption",('Steady','Up','Down','No'),key="option7")
    diabetesMed = st.selectbox("Enter whether Metformin is consumed",('Yes','No'))
    
    if st.button("Click to Predict the need of re-admittance"):
        result = predict(np.array([race,gender,age,number_diagoneses,weight,metformin,glimepiriide,glipizide,glyburide,pioglitazone,rosiglitazone,insulin,diabetesMed]))
        st.text(result[0])

if_name_=='_main_':
    main()
