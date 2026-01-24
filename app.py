import streamlit as st
import pandas as pd

class Calc:
    def __init__(self, v, j, p):
        self.v = v
        self.i = (j / 100) / 12
        self.n = p * 12
    def res(self):
        if self.i == 0: return self.v / self.n
        return self.v * (self.i * (1 + self.i)**self.n) / ((1 + self.i)**self.n - 1)

st.set_page_config(page_title="Kelvin Pro")
st.title("💼 Central Kelvin Pro")
st.write("CRECI-SC: 49891 F")

a1, a2, a3 = st.tabs(["Simulador", "WhatsApp", "Agenda"])

with a1:
    v = st.number_input("Valor", value=250000.0)
    j = st.number_input("Juros %", value=10.5)
    p = st.slider("Anos", 1, 35, 20)
    k = Calc(v, j, p)
    st.metric("Parcela", f"R$ {k.res():,.2f}")

with a2:
    n = st.text_input("Cliente")
    msg = f"Ola {n}, sou o Kelvin. Como posso ajudar?"
    st.info(msg)
    st.markdown(f"[📲 Enviar](https://wa.me/?text={msg.replace(' ', '%20')})")

with a3:
    if 'data' not in st.session_state: st.session_state.data = []
    item = st.text_input("Lead")
    if st.button("Add"): st.session_state.data.append(item)
    for x in st.session_state.data: st.success(f"✅ {x}")
