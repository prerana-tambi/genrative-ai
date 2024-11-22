import streamlit as st

# Correct usage of set_page_config with 'page_title' argument
st.set_page_config(page_title='GEN AI GENERATOR', layout='wide')

# Add your app content below
st.title('Welcome to GEN AI GENERATOR!')
st.write("This is a simple AI generation app.")

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemeini-flash-1.5')

def my_output(query) -> str:
    response = model.generate_content