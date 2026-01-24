import streamlit as st

st.set_page_config(page_title="Kelvin Pro", layout="centered")

# CSS para criar os cards coloridos que você quer
st.markdown("""
    <style>
    .card-urgente { background-color: #ff4b4b; color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .card-visita { background-color: #007bff; color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .card-retorno { background-color: #28a745; color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .whatsapp-btn { background-color: #25d366; color: white; text-align: center; padding: 10px; border-radius: 20px; text-decoration: none; display: block; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 Sistema Kelvin | Inteligência Imobiliária")
st.write(f"**Corretor:** Kelvin Eiyng | **CRECI-SC:** 49891 F")

aba1, aba2, aba3 = st.tabs(["📊 Simulador", "🚀 Atendimento", "🗓️ Minha Agenda"])

with aba1:
    st.subheader("Simulador de Venda")
    v = st.number_input("Valor do Imóvel", value=250000.0)
    st.info(f"Cálculos rápidos para o cliente: R$ {v:,.2f}")

with aba2:
    st.subheader("Modelos de Atendimento")
    nome = st.text_input("Nome do Cliente")
    msg = f"Ola {nome}, sou o Kelvin. Podemos conversar sobre o imovel?"
    st.markdown(f'<a href="https://wa.me/?text={msg}" class="whatsapp-btn">📲 ENVIAR AGORA PARA WHATSAPP</a>', unsafe_allow_html=True)

with aba3:
    st.subheader("⏰ HORA DE FALAR COM:")
    
    # Simulando os cards das suas imagens
    st.markdown('<div class="card-urgente">🚨 <b>URGENTE:</b> João Silva!</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-visita">📅 <b>VISITA:</b> Maria Oliveira (15:30)</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-retorno">📞 <b>RETORNAR:</b> Pedro Santos (16:00)</div>', unsafe_allow_html=True)
