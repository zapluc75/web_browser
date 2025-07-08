import streamlit as st

st.set_page_config(page_title="Central de Aplicativos DER-DF", page_icon="🧰", layout="wide")

# CSS para título e responsividade
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            color: #003366;
            margin-bottom: 10px;
        }
        @media (max-width: 768px) {
            .main-title {
                font-size: 1.4em;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com imagens e título centralizado
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.image("brasao_fisc.png", use_column_width=True)

with col2:
    st.markdown("<div class='main-title'>🧰 Central de Aplicativos DER-DF</div>", unsafe_allow_html=True)

with col3:
    st.image("brasao_der.png", use_column_width=True)

st.markdown("---")

# Links dos aplicativos
st.markdown("""
### 📄 [Merge de PDFs](https://pdfmerge-software001.streamlit.app/)
### 📦 [Pesos e Dimensões](https://pesosedimensoes-software002.streamlit.app/)
""")

st.markdown("---")
st.markdown("🔗 Desenvolvido por Luc • Apps hospedados via Streamlit Cloud")
