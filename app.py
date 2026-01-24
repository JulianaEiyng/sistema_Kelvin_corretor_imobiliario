import streamlit as st

# Configuração da Página para parecer um App Móvel
st.set_page_config(page_title="Kelvin Pro", layout="centered")

# Estilo CSS para criar os cards idênticos às suas fotos
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .header-app { background-color: #1e56a0; color: white; padding: 15px; border-radius: 0 0 15px 15px; text-align: center; margin:-50px -10px 20px -10px; }
    .agenda-title { font-weight: bold; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; }
    .card { border-radius: 12px; padding: 15px; margin-bottom: 12px; background: white; border: 2px solid #eee; display: flex; justify-content: space-between; align-items: center; }
    .card-urgente { border: 2px solid #ff4b4b; }
    .card-visita { border: 2px solid #007bff; }
    .card-retorno { border: 2px solid #28a745; }
    .tag { font-weight: bold; font-size: 12px; }
    .btn-whatsapp { background-color: #111; color: white; text-align: center; padding: 15px; border-radius: 30px; font-weight: bold; margin-top: 20px; cursor: pointer; display: block; text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)

# Topo do Aplicativo
st.markdown('<div class="header-app"><h2>🏠 Kelvin Pro</h2><p>Central do Corretor</p></div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔹 Simulador", "🔹 Atendimento", "🔹 Minha Agenda"])

with tab3:
    st.markdown('<div class="agenda-title">📝 Minha Agenda</div>', unsafe_allow_html=True)
    
    # Card Urgente (Vermelho)
    st.markdown("""
    <div class="card card-urgente">
        <div><b>14:49 - João Silva</b><br><span style="color:#ff4b4b" class="tag">● URGENTE</span></div>
        <div style="color:#ff4b4b; font-size:24px;">⭕</div>
    </div>
    """, unsafe_allow_html=True)

    # Card Visita (Azul)
    st.markdown("""
    <div class="card card-visita">
        <div><b>15:30 - Maria Oliveira</b><br><span style="color:#007bff" class="tag">● VISITA</span></div>
        <div style="color:#007bff; font-size:24px;">⭕</div>
    </div>
    """, unsafe_allow_html=True)

    # Card Retorno (Verde)
    st.markdown("""
    <div class="card card-retorno">
        <div><b>16:00 - Pedro Santos</b><br><span style="color:#28a745" class="tag">● RETORNAR</span></div>
        <div style="color:#28a745; font-size:24px;">⭕</div>
    </div>
    """, unsafe_allow_html=True)

# Botão WhatsApp no estilo da foto
st.markdown('<a href="#" class="btn-whatsapp">💬 ENVIAR AGORA PARA WHATSAPP</a>', unsafe_allow_html=True)

with tab1:
    st.subheader("Simulador de Venda")
    st.number_input("Valor do Imóvel", value=250000.0)

with tab2:
    st.subheader("Atendimento")
    st.text_input("Nome do Cliente")
