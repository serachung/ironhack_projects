import streamlit as st
import numpy as numpy
import pandas as pd 
import plotly_express as px
import seaborn as sns
import speech_recognition as sr

# Para rodar localmente ir na pasta do arquivo através do cmd e 
# rodar o comando streamlit run app.py

st.title('un-dazzled')
st.header('the inverse music recommendation system')
st.subheader ('We support the locals, we support small amateur music artists')
st.write('how it works? throught un-dazzled, you tell us a song you like, and we recommend you a similar song from an amateur singer')

st.subheader ('Choose the way you want to input the song you would like us to recommend')


by_text = st.checkbox('I want to TYPE the Song\'s information')
by_voice = st.checkbox('I want to SPEAK the Song\'s information')
user_input = None

if by_text:
    st.write('Ok, type below the song\'s information:')
    user_input = st.text_input('Name of song')

    st.subheader(f'Your choice was: {user_input} :smile:')

if by_voice:
    user_input = get_audio()
    st.subheader(f'Your choice was: {user_input} :smile:')

#if __name__ == '__main__':
#    main()