import streamlit as st
import speech_recognition as sr
import numpy as numpy
import pandas as pd 

def get_audio():
    import speech_recognition as sr
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write('Speak out loud the title of a song you like :)')

        # read the audio data from the default microphone
        st.write("Listening...")

        audio_data = r.record(source, duration=10)

        # select language
        #language = str(input('Selecione o idioma da música que você gosta'))
        language = 'pt-PT'

        # convert speech to text
        st.write("Processing...")
        user_input = r.recognize_google(audio_data, language=f"{language}")
        st.write(user_input)

        # assuring if it got correctly: 
        answer = str(input(f'Is {user_input} what you meant? (y/n)'))
        if answer in ['y', 'yes', 'Y', 'Yes', 'YES']:
            st.write('Wait a moment while we look for similar songs :)')

    return user_input


st.title('Audio')

by_name = st.checkbox('Input name of song')
by_voice = st.checkbox('By voice')
user_input = None

if by_name:
    st.write('Button was pressed')
    # codigo do menino de 12 anos

    # user_input ...
    user_input = st.text_input('Name of song')

    st.subheader(f'Your choice was: {user_input} :smile:')

if by_voice:
    user_input=check_input(song_input=get_audio('title'), 
                            artist_input=get_audio('artist'))
    user_input = get_audio()
    st.subheader(f'Your choice was: {user_input} :smile:')