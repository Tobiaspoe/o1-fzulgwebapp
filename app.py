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

st.set_page_config(page_title="Förderantrag KI", layout="centered")
st.title("📄 Förderantrag Generator (Modell: o1)")

username = st.text_input("Benutzername")
password = st.text_input("Passwort", type="password")

if username != os.getenv("APP_USERNAME") or password != os.getenv("APP_PASSWORD"):
    st.warning("Ungültige Zugangsdaten.")
    st.stop()

user_input = st.text_area("Was soll das Modell bearbeiten?")

if st.button("Antwort generieren"):
    with st.spinner("Antwort wird generiert..."):
        response = openai.ChatCompletion.create(
            engine=deployment,
            messages=[
                {"role": "system", "content": "Du bist ein Experte für Förderanträge."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(response.choices[0].message["content"])
