import streamlit as st

st.set_page_config(page_title="Central de Aplicativos DER-DF", page_icon="🧰", layout="wide")

# CSS para título e controle de tamanho da imagem
st.markdown("<div class='main-title'>🧰 Central de Aplicativos DER-DF</div>", unsafe_allow_html=True)
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
            max-width: 45px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        @media (max-width: 768px) {
            .main-title {
                font-size: 1.4em;
            }
            .logo-img {
                max-width: 30px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com imagens e título centralizado
col1, col2, col3 = st.columns([2, 0.5, 2])

with col2:
    
   st.image("brasao_der.png", use_container_width=True)
 

st.markdown("---")

# Links dos aplicativos
col_l, col_c, col_r = st.columns([1,1.5,1])  # Botão centralizado usando colunas
with col_c:
   st.markdown("""
   ### 📦 [Pesos e Dimensões](https://Pesos-Dimensoes-software002.streamlit.app/)
   ### 🔐 [Gerar Usuário PeD](https://gerar-senha-software004.streamlit.app/)
   ### 📊 [Gráfico GEOPE](https://graficogeopepowerbi.streamlit.app/)
   """)

st.markdown("---")
st.markdown("🔗 Desenvolvido por Luc • Apps hospedados via Streamlit Cloud")

















