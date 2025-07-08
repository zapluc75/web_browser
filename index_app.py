import streamlit as st

st.set_page_config(page_title="Central de Aplicativos", page_icon="🧰", layout="wide")

# Layout de colunas para os brasões
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.image("Brasao fisc sem fundo.png", use_column_width=True)

with col2:
    st.markdown("<h1 style='text-align: center;'>🧰 Central de Aplicativos DER-DF</h1>", unsafe_allow_html=True)

with col3:
    st.image("Brasao sem fundo 2.png", use_column_width=True)

st.markdown("---")

st.markdown("Escolha uma ferramenta abaixo:")

# Links para os aplicativos
st.markdown("### 📄 [Merge de PDFs](https://pdfmerge-software001.streamlit.app/)")
st.markdown("### 📦 [Pesos e Dimensões](https://pesosedimensoes-software002.streamlit.app/)")

st.markdown("---")
st.markdown("🔗 Desenvolvido por Luc • Apps hospedados via Streamlit Cloud")