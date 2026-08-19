import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from win32com.client import Dispatch
import pythoncom 
import pandas as pd

st.set_page_config(page_title="Spam Detection App", layout="centered") 

def speak(text): 
        pythoncom.CoInitialize()
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(text)
        pythoncom.CoUninitialize()

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))

def main():
	st.title("Email Spam Dectetion App:")
	st.write("Build with Streamlit & Python")
	activites=["Choose an option","Classification"]
	choices=st.sidebar.selectbox("Select Activities",activites)
	if choices=="Classification":
		st.subheader("Classification")
		msg=st.text_input("Enter a text")
		if st.button("Process"):
			print(msg)
			print(type(msg))
			data=[msg]
			print(data)
			vec=cv.transform(data).toarray()
			result=model.predict(vec)
			if result[0]==0:
				st.success("This is not a spam Email")
				speak("This is not a spam Email")
			else:
				st.error("This is a spam Email")
				speak("This is a spam Email")
    
main()  

st.markdown(
      """
      <style>
      [data-testid="stSidebar"] {
          background-color: #A52A2A;
      }
      </style>
      """,
      unsafe_allow_html=True
) 
 
        


