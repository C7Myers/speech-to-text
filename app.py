# streamlit_app.py
import streamlit as st
from gtts import gTTS
import os
from io import BytesIO

st.title("📚 Paper Reader (Text-to-Speech)")

text = st.text_area("Paste your text or paper here:")

if st.button("🔊 Read Aloud"):
    if text.strip() == "":
        st.warning("Please paste some text first.")
    else:
        tts = gTTS(text, lang='en')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        st.audio(mp3_fp, format='audio/mp3')

