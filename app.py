import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from urllib.parse import quote

# 1. Configuração e Estilo
st.set_page_config(page_title="Kelvin Eiyng", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .header-blue { background-color: #1e56a0; color: white; padding: 20px; border-radius: 5px; text-align: center; margin-bottom: 25px; font-weight: bold; font-size: 20px; }
    .card-agenda { background: white; border-radius: 12px; padding: 18px; margin-bottom: 12px; border-left: 10px solid; box-shadow: 0px 4px 6px rgba(0,0,0,0.05); }
    .btn-wa { background-color: #000000; color: white !important; text-align: center; padding: 15px; border-radius: 30px; font-weight: bold; text-decoration: none; display: block; margin: 10px 0; }
    .resumo-calc { background-color: #e3f2fd; padding: 15px; border-radius: 10px; border: 1px solid #1e56a0; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<div class="header-blue">🏠 Kelvin Eiyng | CRECI-SC: 49891 F</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Simulador Completo", "🚀 Atendimento", "🗓️ Minha Agenda"])

with tab1:
    st.subheader("Simulador SAC vs PRICE Profissional")
    col1, col2 = st.columns(2)
    with col1:
        v_imovel = st.number_input("Valor do Financiamento (R$)", value=250000.0, step=1000.0)
        taxa_anual = st.number_input("Taxa de Juros Anual (%)", value=10.5)
    with col2:
        anos_f = st.slider("Prazo (Anos)", 1, 35, 20)
        taxas_extras = st.number_input("Taxas/Seguros Mensais (R$)", value=25.0)

    # Cálculos Reais
    n_meses = anos_f * 12
    i_mensal = (taxa_anual / 100) / 12
    meses_array = np.arange(1, n_meses + 1)
    
    # PRICE
    prestacao_price = v_imovel * (i_mensal * (1+i_mensal)**n_meses) / ((1+i_mensal)**n_meses - 1)
    total_price = (prestacao_price + taxas_extras) * n_meses
    
    # SAC (Primeira e Última)
    amortizacao_sac = v_imovel / n_meses
    juros_1 = v_imovel * i_mensal
    prestacao_1_sac = amortizacao_sac + juros_1 + taxas_extras
    total_sac = sum([(amortizacao_sac + (v_imovel - (m-1)*amortizacao_sac)*i_mensal + taxas_extras) for m in meses_array])

    # Gráfico
    curva_price = [prestacao_price + taxas_extras for _ in meses_array]
    curva_sac = [(amortizacao_sac + (v_imovel - (m-1)*amortizacao_sac)*i_mensal + taxas_extras) for m in meses_array]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses_array, y=curva_price, name='PRICE', line=dict(color='#ff4b4b', width=3)))
    fig.add_trace(go.Scatter(x=meses_array, y=curva_sac, name='SAC', line=dict(color='#1e56a0', width=3)))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    <div class="resumo-calc">
        <b>Resumo do Investimento:</b><br>
        • Total Pago (PRICE): R$ {total_price:,.2f}<br>
        • Total Pago (SAC): R$ {total_sac:,.2f}<br>
        • Economia Estimada na SAC: <b>R$ {(total_price - total_sac):,.2f}</b>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.subheader("Gerador de Proposta")
    n_cliente = st.text_input("Nome do Cliente")
    tel_cliente = st.text_input("WhatsApp (DDD + Número)")
    
    if n_cliente and tel_cliente:
        texto = quote(f"Olá {n_cliente}, aqui é o Kelvin Eiyng. Segue o resumo da simulação:\nValor: R$ {v_imovel:,.2f}\nPrazo: {anos_f} anos\nEconomia na SAC: R$ {(total_price - total_sac):,.2f}")
        st.markdown(f'<a href="https://wa.me/55{tel_cliente}?text={texto}" class="btn-wa">📩 ENVIAR PROPOSTA COMPLETA</a>', unsafe_allow_html=True)

with tab3:
    st.subheader("Marcar Compromisso")
    # Agora o corretor pode digitar!
    c_nome = st.text_input("Nome do Cliente na Agenda")
    c_hora = st.text_input("Horário (ex: 14:30)")
    c_tipo = st.selectbox("Tipo de Compromisso", ["URGENTE", "VISITA", "RETORNAR"])
    
    cores = {"URGENTE": "#ff4b4b", "VISITA": "#007bff", "RETORNAR": "#28a745"}
    
    if st.button("Adicionar à Lista"):
        st.session_state['agenda'] = st.session_state.get('agenda', [])
        st.session_state['agenda'].append({"nome": c_nome, "hora": c_hora, "tipo": c_tipo})

    st.write("---")
    # Exibe o que ele marcou
    if 'agenda' in st.session_state:
        for item in st.session_state['agenda']:
            st.markdown(f'<div class="card-agenda" style="border-left-color: {cores[item["tipo"]]};"><b>{item["hora"]} - {item["nome"]}</b><br><small>STATUS: {item["tipo"]}</small></div>', unsafe_allow_html=True)
