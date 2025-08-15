import streamlit as st

st.set_page_config(page_title="Central de Aplicativos DER-DF", page_icon="🧰", layout="wide")

# CSS para título e controle de tamanho da imagem
st.markdown("""
   <style>
        .main-title {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            color: #003366;
            margin-bottom: 10px;
        }
        .logo-img {
            max-width: 75px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        @media (max-width: 768px) {
            .main-title {
                font-size: 1.4em;
            }
            .logo-img {
                max-width: 60px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com imagens e título centralizado
col1, col2, col3, col4, col5 = st.columns([1, 0.5, 2, 0.5, 1])

with col2:
   st.image("brasao_fisc.png", use_container_width=True)
    

with col3:
    st.markdown("<div class='main-title'>🧰 Central de Aplicativos DER-DF</div>", unsafe_allow_html=True)

 
with col4:
   st.image("brasao_der.png", use_container_width=True)

st.markdown("---")

# Links dos aplicativos
st.markdown("""
### 📄 [Merge de PDFs](https://pdfmerge-software001.streamlit.app/)
### 📦 [Pesos e Dimensões](https://Pesos-Dimensoes-software002.streamlit.app/)
### 📄 [Cronotacógrafo](https://cronotacografo.rbmlq.gov.br/certificados/consultar)
""")

st.markdown("---")
st.markdown("🔗 Desenvolvido por Luc • Apps hospedados via Streamlit Cloud")

