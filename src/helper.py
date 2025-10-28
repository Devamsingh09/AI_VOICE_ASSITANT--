import speech_recognition as sr
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from gtts import gTTS
load_dotenv()


GOOGLE_API_KEY =os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY



def voice_input():
    r=sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print('Adjusting for ambient noise...')
            r.adjust_for_ambient_noise(source, duration=1)
            print('Listening... (Speak now)')
            audio=r.listen(source, timeout=5, phrase_time_limit=10)

        print('Recognizing...')
        text=r.recognize_google(audio)
        print("You said : ",text)
        return text
    except sr.UnknownValueError:
        print("Sorry could not understand the audio")
        return None
    except sr.RequestError as e:
        print('Could not request result from service.')
        return None
    except sr.WaitTimeoutError:
        print("Listening timed out.")
        return None

def llm_model(user_text):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)
    response = llm.invoke(user_text)
    result = response.content
    return result


def text_to_speech(text):
    tts=gTTS(text=text,lang='en')
    tts.save('speech.mp3')
