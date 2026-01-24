import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from urllib.parse import quote
from datetime import datetime, timedelta

# Configurações de Estilo Profissional
st.set_page_config(page_title="Kelvin Eiyng", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .header-blue { background-color: #1e56a0; color: white; padding: 20px; border-radius: 5px; text-align: center; margin-bottom: 25px; font-weight: bold; font-size: 20px; }
    .card-valor { background: white; border: 1px solid #ddd; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    .label-v { font-size: 14px; color: #666; font-weight: bold; }
    .valor-v { font-size: 20px; color: #1e56a0; font-weight: bold; }
    .btn-wa { background-color: #000000; color: white !important; text-align: center; padding: 15px; border-radius: 30px; font-weight: bold; text-decoration: none; display: block; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<div class="header-blue">🏠 Kelvin Eiyng | CRECI-SC: 49891 F</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Simulador", "🚀 Atendimento", "🗓️ Minha Agenda"])

with tab1:
    # Entradas de dados
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        v_finan = st.number_input("Valor Financiado (R$)", value=250000.0)
        juros_a = st.number_input("Juros Anual (%)", value=10.5)
    with col_in2:
        anos_p = st.slider("Prazo (Anos)", 1, 35, 20)
        data_1 = st.date_input("1º Vencimento", datetime.now() + timedelta(days=30))

    # Cálculos
    n = anos_p * 12
    i = (juros_a / 100) / 12
    
    # PRICE
    p_price = v_finan * (i * (1+i)**n) / ((1+i)**n - 1)
    total_price = p_price * n
    
    # SAC
    amort = v_finan / n
    p1_sac = amort + (v_finan * i)
    p_u_sac = amort + (amort * i)
    total_sac = (p1_sac + p_u_sac) * n / 2

    # --- DESTAQUE DE VALORES (ANTES DO GRÁFICO) ---
    st.write("### 🏠 Resumo da Simulação")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="card-valor"><span class="label-v">1ª Parcela (SAC)</span><br><span class="valor-v">R$ {p1_sac:,.2f}</span></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="card-valor"><span class="label-v">Parcela (PRICE)</span><br><span class="valor-v" style="color:#ff4b4b;">R$ {p_price:,.2f}</span></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="card-valor"><span class="label-v">Vencimento</span><br><span class="valor-v" style="color:#28a745;">{data_1.strftime("%d/%m/%y")}</span></div>', unsafe_allow_html=True)
    
    st.write("") # Espaço
    st.info(f"💰 Total Parcelado (SAC): R$ {total_sac:,.2f}  |  Economia: R$ {(total_price - total_sac):,.2f}")

    # Gráfico vem depois
    meses_arr = np.arange(1, n + 1)
    c_sac = [amort + (v_finan - (m-1)*amort)*i for m in meses_arr]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses_arr, y=c_sac, name='SAC', line=dict(color='#1e56a0')))
    fig.add_trace(go.Scatter(x=meses_arr, y=[p_price]*n, name='PRICE', line=dict(color='#ff4b4b', dash='dash')))
    fig.update_layout(height=250, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Atendimento")
    n_c = st.text_input("Nome do Cliente")
    t_c = st.text_input("WhatsApp")
    if n_c and t_c:
        link = quote(f"Olá {n_c}, sou o Kelvin.\n\nSimulação:\n- 1ª Parcela (SAC): R$ {p1_sac:,.2f}\n- Parcela (PRICE): R$ {p_price:,.2f}\n- 1º Vencimento: {data_1.strftime('%d/%m/%Y')}\n- Economia na SAC: R$ {(total_price - total_sac):,.2f}")
        st.markdown(f'<a href="https://wa.me/55{t_c}?text={link}" class="btn-wa">📲 ENVIAR SIMULAÇÃO AGORA</a>', unsafe_allow_html=True)

with tab3:
    st.subheader("Agenda")
    # (Sistema de agenda simplificado)
    st.write("Agende visitas e retornos aqui.")
