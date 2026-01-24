import streamlit as st
import pandas as pd
from datetime import datetime

class KelvinSistema:
    def __init__(self, valor, juros, prazo):
        self.valor = valor
        self.taxa_mensal = (juros / 100) / 12
        self.total_meses = prazo * 12
    def calcular_parcela(self):
        i, n = self.taxa_mensal, self.total_meses
        if i == 0: return self.valor / n
        return self.valor * (i * (1 + i)**n) / ((1 + i)**n - 1)
    def dados_grafico(self):
        p = self.calcular_parcela()
        return pd.DataFrame({"Parcela": [p] * 12})

st.set_page_config(page_title="Kelvin Eiyng", layout="centered")

if 'agenda' not in st.session_state:
    st.session_state.agenda = []

st.title("💼 Central Kelvin Pro")
st.markdown(f"**Corretor:** Kelvin Eiyng | **CRECI-SC:** 49891 F")
st.markdown("---")

t1, t2, t3 = st.tabs(["📊 Simulador", "🚀 WhatsApp", "🗓️ Agenda"])

with t1:
    v = st.number_input("Valor R$", value=250000.0)
    j = st.number_input("Juros Anual %", value=10.5)
    p = st.slider("Anos", 1, 35, 20)
    s = KelvinSistema(v, j, p)
    st.metric("Parcela PRICE", f"R$ {s.calcular_parcela():,.2f}")
    st.line_chart(s.dados_grafico())

with t2:
    n = st.text_input("Nome do Cliente:")
    ass = f"\n\nAtenciosamente,\nKelvin Eiyng\nCRECI-SC 49891 F"
    op = st.selectbox("Mensagem:", ["Boas vindas", "Video", "Docs"])
    txt = f"Ola {n}, como posso ajudar?" + ass
    st.info(txt)
    link = f"https://wa.me/?text={txt.replace(' ', '%20').replace('\n', '%0A')}"
    st.markdown(f"[📲 ENVIAR AGORA]({link})")

with t3:
    c = st.text_input("Lead")
    h = st.time_input("Hora")
    if st.button("Salvar"):
        st.session_state.agenda.append({"n": c, "h": h})
    for i in st.session_state.agenda:
        st.write(f"⏰ {i['h']} - {i['n']}")
