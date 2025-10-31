# -*- coding: utf-8 -*-
import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# =========================
# Configuración de la página
# =========================
st.set_page_config(
    page_title="🧠 Text Analyzer | Tech Mode",
    page_icon="🤖",
    layout="centered"
)

# =========================
# Estilos Tech (oscuro + neón)
# =========================
st.markdown("""
<style>
  :root{
    --bg:#0b1220;
    --panel:#0f182b;
    --text:#e6f7ff;
    --muted:#9fb3c8;
    --accent:#00e5ff;
    --accent2:#00ffa3;
  }
  html, body, .stApp{
    background: radial-gradient(1000px 600px at 10% 0%, #0f1a30 0%, var(--bg) 60%);
    color: var(--text) !important;
  }
  [data-testid="stSidebar"], section[data-testid="stSidebar"] > div{
    background: linear-gradient(180deg, #0e1628 0%, #0b1220 100%) !important;
    color: var(--text) !important;
    border-right: 1px solid rgba(0,229,255,.15);
  }
  h1,h2,h3,h4,h5,h6{
    color: var(--accent);
    font-family: "JetBrains Mono", monospace;
  }
  p, label, span, div, .stMarkdown{
    color: var(--text) !important;
    font-family: "Inter", sans-serif;
  }
  .stButton>button{
    background: linear-gradient(90deg, var(--accent) 0%, var(--accent2) 100%) !important;
    color: #00121a !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    transition: transform .08s ease-in-out, box-shadow .2s ease-in-out;
    box-shadow: 0 0 12px rgba(0,229,255,.5);
  }
  .stButton>button:hover{
    transform: translateY(-1px);
    box-shadow: 0 0 18px rgba(0,229,255,.75);
  }
  textarea, input{
    background: #0f182b !important;
    color: var(--text) !important;
    border: 1px solid rgba(0,229,255,.3) !important;
    border-radius: 10px !important;
  }
  .stExpander{
    background: var(--panel) !important;
    border: 1px solid rgba(0,229,255,.2);
    border-radius: 10px;
  }
</style>
""", unsafe_allow_html=True)

# =========================
# Inicializar traductor
# =========================
translator = Translator()

# =========================
# Título y descripción
# =========================
st.title("🤖 Text Analyzer | Tech Mode")
st.markdown("""
Analiza tus textos con **IA lingüística** usando `TextBlob` y `Google Translator` 🌐  
Mide **polarity** (sentimiento) y **subjectivity** (opinión vs hecho).  
_Tecnología aplicada al lenguaje humano ⚙️_
""")

# =========================
# Barra lateral (info técnica)
# =========================
with st.sidebar:
    st.subheader("🧠 Polarity & Subjectivity")
    st.markdown("""
    - **Polarity:** Evalúa el sentimiento del texto entre -1 (negativo) y 1 (positivo).  
    - **Subjectivity:** Mide el nivel de opinión o emoción (0 objetivo → 1 subjetivo).  
    - **Modelo:** `TextBlob` con análisis semántico básico.  
    - **Traducción:** `GoogleTranslator` automático de español → inglés. 🌍
    """)

# =========================
# Expander principal
# =========================
with st.expander("⚙️ Analyze Sentiment & Subjectivity"):
    text1 = st.text_area("💬 Enter your text (in Spanish):", placeholder="Escribe aquí el texto a analizar...")
    if text1:
        try:
            with st.spinner("🧠 Processing... Translating and analyzing sentiment..."):
                translation = translator.translate(text1, src="es", dest="en")
                trans_text = translation.text
                blob = TextBlob(trans_text)
                
                polarity = round(blob.sentiment.polarity, 2)
                subjectivity = round(blob.sentiment.subjectivity, 2)

            st.markdown("---")
            st.subheader("📊 Results")
            st.write(f"**Polarity:** `{polarity}`")
            st.write(f"**Subjectivity:** `{subjectivity}`")

            if polarity >= 0.5:
                st.success("✅ Positive Sentiment Detected 😎")
            elif polarity <= -0.5:
                st.error("⚠️ Negative Sentiment Detected 😠")
            else:
                st.info("🧩 Neutral Sentiment 😐")

            if subjectivity > 0.5:
                st.caption("🗣️ The text is quite **subjective** (emotional/opinionated).")
            else:
                st.caption("📘 The text is rather **objective** (fact-based).")

        except Exception as e:
            st.error(f"⚠️ Error analyzing text: {e}")

# =========================
# Expander de corrección
# =========================
with st.expander("🧩 English Correction (Grammar AI)"):
    text2 = st.text_area("✏️ Enter text in English:", placeholder="Write a sentence to correct...", key="text2")
    if text2:
        blob2 = TextBlob(text2)
        corrected = blob2.correct()
        st.markdown("### ✅ Corrected version:")
        st.success(corrected)

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown("""
**Tech Mode Linguistic Analyzer 🧠**  
Built with **TextBlob + Streamlit** · Styled with **dark neon UI** ⚙️  
> “Turning words into data, and data into insight.” 💾
""")
