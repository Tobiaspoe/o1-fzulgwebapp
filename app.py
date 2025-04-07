import os
import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

st.set_page_config(page_title="Förderantrag Generator", layout="centered")
st.title("📄 Förderantrag Generator (Modell: o1)")

# Login
username = st.text_input("Benutzername")
password = st.text_input("Passwort", type="password")

if username != os.getenv("APP_USERNAME") or password != os.getenv("APP_PASSWORD"):
    st.warning("Bitte gültige Zugangsdaten eingeben.")
    st.stop()

# Eingabe
user_input = st.text_area("Was soll das Modell bearbeiten?")

if st.button("Antwort generieren"):
    with st.spinner("Modell denkt nach ..."):
        response = openai.ChatCompletion.create(
            engine=deployment,
            messages=[
                {"role": "system", "content": "Du bist ein Experte für Forschungs- und Förderanträge. Antworten präzise, strukturiert und normenkonform."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(response.choices[0].message["content"])
