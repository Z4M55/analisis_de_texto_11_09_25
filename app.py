# =========================
# Estilos personalizados
# =========================
page_bg = """
<style>
    body {
        background-color: #B7E5CD;
        color: #305669;
    }
    .stApp {
        background-color: #B7E5CD;
        color: #305669;
    }
    div[data-testid="stMarkdown"] p, div[data-testid="stHeader"] h1, h2, h3, h4, h5, h6, label, span {
        color: #305669 !important;
    }
    .stButton>button {
        background-color: #305669 !important;
        color: #ffffff !important;
        border: none;
        border-radius: 6px;
    }
    .stButton>button:hover {
        background-color: #24454D !important;
        color: #ffffff !important;
    }
    .stProgress .st-bo {
        background-color: #305669 !important;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
