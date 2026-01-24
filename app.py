import streamlit as st

# Configuração da página
st.set_page_config(page_title="Kelvin Eiyng - Central Pro", layout="centered")

# Visual Profissional (CSS)
st.markdown("""
    <style>
    .main-header { background-color: #1e56a0; color: white; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 20px; }
    .card-agenda { border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: #fcfcfc; border-left: 8px solid #1e56a0; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #25d366; color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

# Topo do Site
st.markdown('<div class="main-header"><h1>🏠 Kelvin Pro</h1><p>Kelvin Eiyng | CRECI-SC: 49891 F</p></div>', unsafe_allow_html=True)

# Abas de navegação
tab1, tab2, tab3 = st.tabs(["📊 Simulador", "🚀 Atendimento", "🗓️ Minha Agenda"])

with tab1:
    st.subheader("Simulador Financeiro")
    valor = st.number_input("Valor do Imóvel (R$)", value=250000.0)
    st.write(f"### Valor Simulado: R$ {valor:,.2f}")

with tab2:
    st.subheader("Atendimento ao Cliente")
    nome_cliente = st.text_input("Nome do Cliente")
    if nome_cliente:
        st.write(f"Olá {nome_cliente}, sou o Kelvin Eiyng. Como posso ajudar?")
    st.button("ENVIAR PARA WHATSAPP")

with tab3:
    st.subheader("Gestão de Agenda")
    st.markdown('<div class="card-agenda"><b>14:49</b> - Retornar para João Silva</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-agenda"><b>15:30</b> - Visita: Maria Oliveira</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-agenda"><b>16:00</b> - Enviar Proposta: Pedro Santos</div>', unsafe_allow_html=True)
