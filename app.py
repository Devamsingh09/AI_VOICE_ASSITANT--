import streamlit as st
from src.helper import llm_model, voice_input, text_to_speech

def main():
    st.title("AI Voice Assistant🤖 (Multilingual)")

    if 'voice_text' not in st.session_state:
        st.session_state.voice_text = None

    if st.button("Start Listening"):
        with st.spinner("Listening...👂"):
            text = voice_input()
            if text:
                st.session_state.voice_text = text
                st.success("Voice input captured!")
                st.write(f"You said: {text}")
            else:
                st.error("Could not understand the audio. Please try again.")

    if st.session_state.voice_text:
        if st.button("Submit"):
            with st.spinner("Processing...🤖"):
                response = llm_model(st.session_state.voice_text)
                text_to_speech(response)

                audio_file = open('speech.mp3', 'rb')
                audio_bytes = audio_file.read()

                st.text_area(label="Response:", value=response, height=390)
                st.audio(audio_bytes)
                st.download_button(label="Download speech",
                                   data=audio_bytes,
                                   file_name="speech.mp3",
                                   mime="audio/mp3")
                # Clear the voice text after processing
                st.session_state.voice_text = None





if __name__=="__main__":
    main()
