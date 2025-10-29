import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import google.generativeai as palm
import os
from dotenv import load_dotenv

# load_dotenv()

# palm.configure(api_key=os.getenv("GOOGLE_API_KEY"))
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

def voice_input():
    mics = sr.Microphone.list_microphone_names()
    if not mics:
        print("No microphone found. Please check your microphone settings.")
        return ""
    # Try to find a suitable microphone (prefer built-in or default)
    mic_index = None
    for i, name in enumerate(mics):
        if 'Microphone Array' in name or 'Microphone' in name:
            mic_index = i
            break
    if mic_index is None:
        mic_index = 0  # Default to first available
    r = sr.Recognizer()
    with sr.Microphone(device_index=mic_index) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print(f"Listening using {mics[mic_index]}... (Speak for up to 10 seconds)")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""
    except sr.WaitTimeoutError:
        print("Listening timed out. No speech detected.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def llm_model(user_text):
    if not user_text.strip():
        return "Sorry, I didn't receive any input. Please try speaking again."
    model = palm.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_text)
    result = response.text
    return result

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")

