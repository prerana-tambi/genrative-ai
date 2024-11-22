from dotenv import load_dotenv 
load_dotenv() 

import streamlit as st 
import os 
import google.generativeai as genai 
# Correct usage of set_page_config with 'page_title' argument
st.set_page_config(page_title='GEN AI GENERATOR', layout='wide')

# Add your app content below
st.title('Welcome to GEN AI GENERATOR!')
st.write("This is a simple AI generation app.")

genai.configure(api_key="AIzaSyDvddt_-PvXxzygmoQkZxp0-e3zUogl21A")

# model = genai.GenerativeModel("gemini-flash-1.5") 
model = genai.GenerativeModel("gemini-pro") 

def my_output(query):
    response = model.generate_content(query) 
    return response.text 

#### UI Development using streamlit 


st.header("SMART_BOT") 
input = st.text_input("Input " , key = "input")  
submit = st.button("Ask your query") 

if submit :
    response = my_output(input) 
    st.subheader("The Response is=")
    st.write(response)
