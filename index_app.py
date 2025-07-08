import streamlit as st

# Configuração da página
st.set_page_config(page_title="Central de Aplicativos DER-DF", page_icon="🧰", layout="wide")

# CSS customizado para responsividade e estilo
st.markdown("""
    <style>
        .centered-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 30px;
            margin-bottom: 10px;
        }
        .logo-img {
            max-width: 140px;
            height: auto;
        }
        .main-title {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            color: #003366;
            margin-bottom: 10px;
        }
        .app-card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            text-align: center;
            font-size: 1.1em;
            transition: transform 0.2s ease;
        }
        .app-card:hover {
            transform: scale(1.02);
            background-color: #e4e8ee;
        }
        .app-link {
            text-decoration: none;
            color: #0c5ca3;
            font-weight: bold;
        }
        @media (max-width: 768px) {
            .logo-img {
                max-width: 100px;
            }
            .main-title {
                font-size: 1.5em;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com brasões e título
st.markdown("""
<div class="centered-container">
    <img src="F1.jpg" class="logo-img" >
    <div class="main-title">🧰 Central de Aplicativos DER-DF</div>
    <img src="Brasao_f2.png" class="logo-img" alt="Departamento DER-DF">
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Cartões com links dos apps
st.markdown("""
<div class="centered-container">
    <div class="app-card">
        <a href="https://pdfmerge-software001.streamlit.app/" target="_blank" class="app-link">
            📄 Merge de PDFs
        </a>
    </div>
    <div class="app-card">
        <a href="https://pesosedimensoes-software002.streamlit.app/" target="_blank" class="app-link">
            📦 Pesos e Dimensões
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("🔗 Desenvolvido por Luc • Apps hospedados via Streamlit Cloud", unsafe_allow_html=True)
