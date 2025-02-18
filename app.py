import streamlit as st
from src.helper import llm_model, voice_input, text_to_speech




def main():
    st.title("AI Voice Assistant🤖 (Multilingual)")
    if st.button("Ask me anything !"):
        with st.spinner("Listening...👂"):
            text = voice_input()
            response = llm_model(text)
            text_to_speech(response)

            audio_file = open('speech.mp3', 'rb')
            audio_bytes = audio_file.read()


            st.text_area(label = "Response:", value=response, height=390)
            st.audio(audio_bytes)
            st.download_button(label="Download speech",
                               data = audio_bytes,
                               file_name="speech.mp3",
                               mime = "audio/mp3")





if __name__=="__main__":
    main()