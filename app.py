import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from urllib.parse import quote

# 1. Configuração e Visual Profissional
st.set_page_config(page_title="Kelvin Eiyng", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .header-blue { background-color: #1e56a0; color: white; padding: 20px; border-radius: 5px; text-align: center; margin-bottom: 25px; font-weight: bold; font-size: 20px; }
    .card-agenda { background: white; border-radius: 12px; padding: 18px; margin-bottom: 12px; border-left: 10px solid; box-shadow: 0px 4px 6px rgba(0,0,0,0.05); }
    .btn-wa { background-color: #000000; color: white !important; text-align: center; padding: 15px; border-radius: 30px; font-weight: bold; text-decoration: none; display: block; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho Principal
st.markdown(f'<div class="header-blue">🏠 Kelvin Eiyng | CRECI-SC: 49891 F</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Simulador", "🚀 Atendimento", "🗓️ Minha Agenda"])

with tab1:
    st.subheader("Simulador SAC vs PRICE")
    v_imovel = st.number_input("Valor do Imóvel (R$)", value=250000.0)
    anos = st.slider("Prazo (Anos)", 1, 35, 20)
    
    # Gráfico de Evolução
    n, i = anos * 12, (10.5 / 100) / 12
    meses = np.arange(1, n + 1)
    curva_price = [v_imovel * (i * (1+i)**n) / ((1+i)**n - 1) for _ in meses]
    curva_sac = [(v_imovel/n) + (v_imovel - (m-1)*(v_imovel/n))*i for m in meses]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses, y=curva_price, name='PRICE', line=dict(color='#ff4b4b')))
    fig.add_trace(go.Scatter(x=meses, y=curva_sac, name='SAC', line=dict(color='#1e56a0')))
    fig.update_layout(title="Comparativo de Parcelas", height=300, margin=dict(l=0,r=0,t=40,b=0))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Mensagens Rápidas")
    nome_c = st.text_input("Nome do Cliente")
    fone = st.text_input("WhatsApp (com DDD)", placeholder="47999999999")
    
    if nome_c and fone:
        # Mensagens prontas
        msg1 = quote(f"Olá {nome_c}, aqui é o Kelvin Eiyng. Segue a simulação do seu imóvel que conversamos!")
        msg2 = quote(f"Oi {nome_c}, sou o Kelvin. Podemos agendar uma visita para hoje?")
        
        st.markdown(f'<a href="https://wa.me/55{fone}?text={msg1}" class="btn-wa">📄 ENVIAR SIMULAÇÃO</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://wa.me/55{fone}?text={msg2}" class="btn-wa">📅 AGENDAR VISITA</a>', unsafe_allow_html=True)

with tab3:
    st.subheader("Agenda de Hoje")
    st.markdown('<div class="card-agenda" style="border-left-color: #ff4b4b;"><b>14:49 - João Silva</b><br><small>STATUS: URGENTE</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="card-agenda" style="border-left-color: #007bff;"><b>15:30 - Maria Oliveira</b><br><small>STATUS: VISITA</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="card-agenda" style="border-left-color: #28a745;"><b>16:00 - Pedro Santos</b><br><small>STATUS: RETORNAR</small></div>', unsafe_allow_html=True)

st.write("---")
st.caption("Central de Vendas Kelvin Eiyng")
