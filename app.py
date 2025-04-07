import streamlit as st
import openai

# ------------------ CONFIG ------------------ #
api_key = "8Q3gzvFocgbv0GRUffwU4t0PXicVQ1BoeqXQVzzDzdxiOqYpDw8cJQQJ99BCACfhMk5XJ3w3AAABACOGWQBQ"
azure_endpoint = "https://finmatch-bsfz-sweden-march25-v4.openai.azure.com"
deployment_name = "o1"
api_version = "2024-02-15-preview"

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
            client = openai.AzureOpenAI(
                api_key=api_key,
                api_version=api_version,
                azure_endpoint=azure_endpoint
            )

            response = client.chat.completions.create(
                model=deployment_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=1500
            )

            reply = response.choices[0].message.content
            st.markdown("### 💬 Antwort")
            st.write(reply)
