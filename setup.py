from setuptools import find_packages

setup(
    name="AI Voice Assistant",
    version="0.0.1",
    author="Devam Singh",
    author_email="devamsingh0009@gmail.com",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition==3.14.1",
        "pipwin==0.5.2",
        "pyaudio==0.2.14",
        "gTTS==2.5.4",
        "google-generativeai==0.8.4",
        "python-dotenv==1.0.1",
        "streamlit==1.42.0",
    ],
)
