import streamlit as st
import pandas as pd
from datetime import datetime

class KelvinSistema:
    def __init__(self, v, j, p):
        self.v = v
        self.i = (j / 100) / 12
        self.n = p * 12
    def calcular(self):
        if self.i == 0: return self.v / self.n
        return self.v * (self.i * (1 + self.i)**self.n) / ((1 + self.i)**self.n - 1)

st.set_page_config(page_title="Kelvin Eiyng", layout="centered")

if 'agenda' not in st.session_state:
    st.session_state.agenda = []

st.title("💼 Central Kelvin Pro")
st.write(f"Corretor: Kelvin Eiyng | CRECI-SC: 49891 F")

t1, t2, t3 = st.tabs(["Simulador", "WhatsApp", "Agenda"])

with t1:
    val = st.number_input("Valor R$", value=250000.0)
    jur = st.number_input("Juros %", value=10.5)
    pra = st.slider("Anos", 1, 35, 20)
    k = KelvinSistema(val, jur, pra)
    res = k.calcular()
    st.metric("Parcela", f"R$ {res:,.2f}")

with t2:
    cli = st.text_input("Cliente:")
    msg = f"Ola {cli}, sou o Kelvin. Como posso ajudar?\n\nKelvin Eiyng\nCRECI-SC 49891 F"
    st.text_area("Mensagem:", msg)
    link = f"https://wa.me/?text={msg.replace(' ', '%20').replace('\n', '%0A')}"
    st.markdown(f"[📲 ENVIAR]({link})")

with t3:
    nome = st.text_input("Lead:")
    hora = st.time_input("Hora:")
    if st.button("Salvar"):
        st.session_state.agenda.append({"n": nome, "h": hora})
    for i in st.session_state.agenda:
        st.write(f"⏰ {i['h']} - {i['n']}")
