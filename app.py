import streamlit as st
import pandas as pd

# Sistema de Calculo
class SistemaKelvin:
    def __init__(self, v, j, p):
        self.v = v
        self.i = (j / 100) / 12
        self.n = p * 12
    def calcular(self):
        if self.i == 0: return self.v / self.n
        return self.v * (self.i * (1 + self.i)**self.n) / ((1 + self.i)**self.n - 1)

# Interface do Usuario
st.set_page_config(page_title="Sistema Kelvin", layout="centered")

st.title("💼 Central do Corretor - Kelvin Eiyng")
st.write("CRECI-SC: 49891 F")

aba1, aba2, aba3 = st.tabs(["📊 Simulador", "🚀 WhatsApp", "🗓️ Agenda"])

with aba1:
    val = st.number_input("Valor do Imóvel", value=250000.0)
    jur = st.number_input("Juros Anual %", value=10.5)
    pra = st.slider("Anos", 1, 35, 20)
    k = SistemaKelvin(val, jur, pra)
    st.metric("Parcela Mensal", f"R$ {k.calcular():,.2f}")

with aba2:
    cliente = st.text_input("Nome do Cliente")
    msg = f"Olá {cliente}, aqui é o Kelvin. Como posso ajudar?"
    st.info(msg)
    st.markdown(f"[📲 Enviar para WhatsApp](https://wa.me/?text={msg.replace(' ', '%20')})")

with aba3:
    if 'agenda' not in st.session_state: st.session_state.agenda = []
    novo = st.text_input("Novo compromisso:")
    if st.button("Adicionar"):
        st.session_state.agenda.append(novo)
    for item in st.session_state.agenda:
        st.success(f"✅ {item}")
