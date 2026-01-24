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
    .label-v { font-size: 13px; color: #666; font-weight: bold; }
    .valor-v { font-size: 18px; color: #1e56a0; font-weight: bold; }
    .card-agenda { background: white; border-radius: 12px; padding: 15px; margin-bottom: 10px; border-left: 10px solid; box-shadow: 0px 4px 6px rgba(0,0,0,0.05); }
    .btn-wa { background-color: #000000 !important; color: white !important; text-align: center; padding: 15px; border-radius: 30px; font-weight: bold; text-decoration: none; display: block; margin: 10px 0; border: none; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<div class="header-blue">🏠 Kelvin Eiyng | CRECI-SC: 49891 F</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Simulador", "🚀 Atendimento", "🗓️ Minha Agenda"])

with tab1:
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        v_finan = st.number_input("Valor Financiado (R$)", value=250000.0)
        juros_a = st.number_input("Juros Anual (%)", value=10.5)
    with col_in2:
        anos_p = st.slider("Prazo (Anos)", 1, 35, 20)
        data_1 = st.date_input("1º Vencimento", datetime.now() + timedelta(days=30))

    # Cálculos Reais
    n = anos_p * 12
    i = (juros_a / 100) / 12
    
    # PRICE (Fixa)
    p_price = v_finan * (i * (1+i)**n) / ((1+i)**n - 1)
    total_price = p_price * n
    
    # SAC (Decrescente)
    amort = v_finan / n
    p1_sac = amort + (v_finan * i)
    p_u_sac = amort + (amort * i)
    total_sac = (p1_sac + p_u_sac) * n / 2

    # --- DESTAQUE DE VALORES (O QUE VOCÊ PEDIU) ---
    st.write("### 🏠 Resumo do Financiamento")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="card-valor"><span class="label-v">1ª Parcela (SAC)</span><br><span class="valor-v">R$ {p1_sac:,.2f}</span></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="card-valor"><span class="label-v">Parcela (PRICE)</span><br><span class="valor-v" style="color:#ff4b4b;">R$ {p_price:,.2f}</span></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="card-valor"><span class="label-v">1º Vencimento</span><br><span class="valor-v" style="color:#28a745;">{data_1.strftime("%d/%m/%y")}</span></div>', unsafe_allow_html=True)
    
    st.write("")
    st.success(f"💰 **Total Parcelado (SAC):** R$ {total_sac:,.2f} | **Total Parcelado (PRICE):** R$ {total_price:,.2f}")
    st.info(f"📈 **Economia Real na SAC:** R$ {(total_price - total_sac):,.2f}")

    # Gráfico
    meses_arr = np.arange(1, n + 1)
    c_sac = [amort + (v_finan - (m-1)*amort)*i for m in meses_arr]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses_arr, y=c_sac, name='SAC (Cai todo mês)', line=dict(color='#1e56a0', width=3)))
    fig.add_trace(go.Scatter(x=meses_arr, y=[p_price]*n, name='PRICE (Igual todo mês)', line=dict(color='#ff4b4b', dash='dash')))
    fig.update_layout(height=250, margin=dict(l=0,r=0,t=0,b=0), legend=dict(orientation="h", y=-0.2))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Gerar Proposta WhatsApp")
    n_c = st.text_input("Nome do Cliente")
    t_c = st.text_input("WhatsApp (DDD + Número)")
    if n_c and t_c:
        msg = quote(f"Olá {n_c}, aqui é o Kelvin.\n\nSimulação:\n- 1ª Parc (SAC): R$ {p1_sac:,.2f}\n- Parc (PRICE): R$ {p_price:,.2f}\n- 1º Venc: {data_1.strftime('%d/%m/%Y')}\n- Total (SAC): R$ {total_sac:,.2f}")
        st.markdown(f'<a href="https://wa.me/55{t_c}?text={msg}" class="btn-wa">📲 ENVIAR SIMULAÇÃO AGORA</a>', unsafe_allow_html=True)

with tab3:
    st.subheader("🗓️ Marcar Compromisso")
    
    # Memória para a agenda funcionar
    if 'agenda_kelvin' not in st.session_state:
        st.session_state['agenda_kelvin'] = []

    with st.form("form_agenda"):
        c_nome = st.text_input("Nome do Cliente")
        c_hora = st.text_input("Horário (Ex: 14:00)")
        c_tipo = st.selectbox("Tipo de Atendimento", ["URGENTE", "VISITA", "RETORNAR"])
        btn_salvar = st.form_submit_button("Salvar na Agenda")
        
        if btn_salvar:
            if c_nome and c_hora:
                st.session_state['agenda_kelvin'].append({"nome": c_nome, "hora": c_hora, "tipo": c_tipo})
                st.rerun()

    st.write("---")
    st.subheader("Lista de Hoje")
    
    if not st.session_state['agenda_kelvin']:
        st.write("Nenhum compromisso marcado.")
    else:
        cores = {"URGENTE": "#ff4b4b", "VISITA": "#007bff", "RETORNAR": "#28a745"}
        for item in st.session_state['agenda_kelvin']:
            st.markdown(f"""
            <div class="card-agenda" style="border-left-color: {cores[item['tipo']]};">
                <b>{item['hora']} - {item['nome']}</b><br>
                <small>Status: {item['tipo']}</small>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("Limpar Agenda"):
            st.session_state['agenda_kelvin'] = []
            st.rerun()
