import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. Configuração de Estilo Profissional (CSS)
st.set_page_config(page_title="Kelvin Eiyng", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .header-blue { background-color: #1e56a0; color: white; padding: 20px; border-radius: 5px; text-align: center; margin-bottom: 25px; font-weight: bold; font-size: 20px; }
    .card-agenda { background: white; border-radius: 12px; padding: 18px; margin-bottom: 12px; border-left: 10px solid; box-shadow: 0px 4px 6px rgba(0,0,0,0.05); display: flex; justify-content: space-between; align-items: center; }
    .btn-whatsapp { background-color: #000000; color: white !important; text-align: center; padding: 15px; border-radius: 30px; font-weight: bold; text-decoration: none; display: block; margin-top: 20px; }
    .tag-status { font-weight: bold; font-size: 11px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho Atualizado (Sem "Inteligência Imobiliária")
st.markdown('<div class="header-blue">🏠 Kelvin Eiyng | CRECI-SC: 49891 F</div>', unsafe_allow_html=True)

# 3. Abas
tab1, tab2, tab3 = st.tabs(["📊 Simulador", "🚀 Atendimento", "🗓️ Minha Agenda"])

with tab1:
    st.subheader("Simulador Comparativo: SAC vs PRICE")
    col1, col2 = st.columns(2)
    with col1:
        v_imovel = st.number_input("Valor do Imóvel (R$)", value=250000.0)
        juros = st.number_input("Juros Anual (%)", value=10.5)
    with col2:
        anos = st.slider("Anos", 1, 35, 20)
    
    # Cálculos para o Gráfico
    n = anos * 12
    i = (juros / 100) / 12
    meses_eixo = np.arange(1, n + 1)
    curva_price = [v_imovel * (i * (1+i)**n) / ((1+i)**n - 1) for _ in meses_eixo]
    curva_sac = [(v_imovel/n) + (v_imovel - (m-1)*(v_imovel/n))*i for m in meses_eixo]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses_eixo, y=curva_price, name='PRICE', line=dict(color='#ff4b4b', width=3)))
    fig.add_trace(go.Scatter(x=meses_eixo, y=curva_sac, name='SAC', line=dict(color='#1e56a0', width=3)))
    fig.update_layout(title="Evolução das Parcelas", height=300, margin=dict(l=0,r=0,t=40,b=0))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Atendimento")
    nome = st.text_input("Nome do Cliente")
    if nome:
        st.info(f"Proposta personalizada para {nome}")
    st.markdown('<a href="#" class="btn-whatsapp">💬 ENVIAR AGORA PARA WHATSAPP</a>', unsafe_allow_html=True)

with tab3:
    st.markdown("### 🗓️ Minha Agenda")
    
    st.markdown("""
    <div class="card-agenda" style="border-left-color: #ff4b4b;">
        <div><b>14:49 - João Silva</b><br><span class="tag-status" style="color: #ff4b4b;">● URGENTE</span></div>
        <div style="color: #ff4b4b; font-size: 20px;">⭕</div>
    </div>
    <div class="card-agenda" style="border-left-color: #007bff;">
        <div><b>15:30 - Maria Oliveira</b><br><span class="tag-status" style="color: #007bff;">● VISITA</span></div>
        <div style="color: #007bff; font-size: 20px;">⭕</div>
    </div>
    <div class="card-agenda" style="border-left-color: #28a745;">
        <div><b>16:00 - Pedro Santos</b><br><span class="tag-status" style="color: #28a745;">● RETORNAR</span></div>
        <div style="color: #28a745; font-size: 20px;">⭕</div>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.caption("Central do Corretor | Profissionalismo e Agilidade")
