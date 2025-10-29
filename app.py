import speech_recognition as sr
from gtts import gTTS
import google.generativeai as palm
import os
from dotenv import load_dotenv
import streamlit as st
from src.helper import voice_input, llm_model, text_to_speech


def main():
    st.title("AI VOICE ASSISTANT (Using GEMINI )")
    
    if st.button("Ask me anything"):
        with st.spinner('Listening...'):
            text = voice_input()
            if text:
                response=llm_model(text)
                text_to_speech(response)

                audio_file=open("speech.mp3","rb")
                audio_bytes=audio_file.read()
                st.text_area(label="Response", value=response, height=350)
                st.audio(audio_bytes)

                st.download_button(label="Download speech",data=audio_bytes,
                                   file_name="speech.mp3",
                                   mime='audio/mp3')
            else:
                st.error("No speech detected or recognized. Please try again.")
            
if __name__=="__main__":
    main()
            
