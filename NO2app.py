#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("boost_final.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(PP2,WFPS25cm,NH4,PP7,AirT,DAF_TD,Year,NO3,DAF_SD,Month):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=boost_final.predict([[PP2,WFPS25cm,NH4,PP7,AirT,DAF_TD,Year,NO3,DAF_SD,Month]])
    print(prediction)
    return prediction



def main():
    st.title("NO2 Regression")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    PP2 = st.text_input("PP2","Type Here")
    WFPS25cm = st.text_input("WFPS25cm","Type Here")
    NH4 = st.text_input("NH4","Type Here")
    PP7 = st.text_input("PP7","Type Here")
    AirT = st.text_input("AirT","Type Here")
    DAF_TD = st.text_input("DAF_TD","Type Here")
    Year = st.text_input("Year","Type Here")
    NO3 = st.text_input("NO3","Type Here")
    DAF_SD = st.text_input("DAF_SD","Type Here")
    Month = st.text_input("Month","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(PP2,WFPS25cm,NH4,PP7,AirT,DAF_TD,Year,NO3,DAF_SD,Month)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

