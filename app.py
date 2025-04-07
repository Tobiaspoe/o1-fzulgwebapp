import streamlit as st
import openai
import os
import requests

# ------------------ CONFIG ------------------ #
openai.api_key = "8Q3gzvFocgbvUGRUffwU4t0PXicVQ1B0eqXQVzzDzdXiOyYpDw8cJQQJ98BCACfhMk5XJ3w3AAABACOGWBQQ"
openai.api_base = "https://finmatch-bsfz-sweden-march25-v4.openai.azure.com/"
openai.api_type = "azure"
openai.api_version = "2024-02-15-preview"

deployment_name = "o1"  # Dein Azure Deployment-Name
system_prompt = """**Einleitung und Funktion**:
Du erstellst Anträge für die Forschungszulage basierend auf dem vorgegebenen Wissensstand. Du agierst wie ein smarter KI-Förderberater mit Verständnis für Textanalyse, Steuerrichtlinien und Innovationsförderung. Reagiere sachlich, hilfreich und förderlogisch."""

# ------------------ UI ------------------ #
st.set_page_config(page_title="Förder-KI Assistent", layout="wide")
st.title("🤖 Förder-KI Assistent für Forschungszulagen")

user_input = st.text_area("Was möchtest du besprechen?", height=200)

if st.button("Absenden"):
    if user_input.strip() == "":
        st.warning("Bitte eine Eingabe machen.")
    else:
        with st.spinner("KI denkt nach..."):
            response = openai.ChatCompletion.create(
                engine=deployment_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            reply = response.choices[0].message["content"]
            st.markdown("### 💬 Antwort")
            st.write(reply)
