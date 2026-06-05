import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text between multiple languages with extra features.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn"
}

text = st.text_area("Enter Text")

source_lang = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Target Language",
    list(languages.keys())
)

translated = ""

if st.button("Translate"):
    if text.strip():
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Complete!")
        st.text_area("Translated Text", translated, height=150)

        # Copy Button (Streamlit workaround using base64)
        b64 = base64.b64encode(translated.encode()).decode()
        copy_button = f'''
        <a href="data:text/plain;base64,{b64}" download="translated_text.txt">
        📋 Download / Copy Text
        </a>
        '''
        st.markdown(copy_button, unsafe_allow_html=True)

        # Text-to-Speech Feature
        tts = gTTS(translated, lang=languages[target_lang])
        tts.save("speech.mp3")

        audio_file = open("speech.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

    else:
        st.warning("Please enter some text.")
