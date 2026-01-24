import streamlit as st
import pandas as pd
from datetime import datetime

# Classe para cálculos financeiros imobiliários
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
        parcela = self.calcular_parcela()
        return pd.DataFrame({"Evolução": [parcela] * 12})

# Configuração da página e identidade visual
st.set_page_config(page_title="Kelvin Eiyng - Inteligência Imobiliária", layout="centered")

# Estado da agenda para manter dados durante a sessão
if 'agenda_contatos' not in st.session_state:
    st.session_state.agenda_contatos = []

# Cabeçalho Profissional
st.title("💼 Central Kelvin Pro")
st.markdown(f"**Corretor:** Kelvin Eiyng | **CRECI-SC:** 49891 F")
st.markdown("---")

# Organização por abas para uso em dispositivos móveis
aba_simulador, aba_atendimento, aba_agenda = st.tabs([
    "📊 Simulador", "🚀 Mensagens Rápidas", "🗓️ Agenda & Alarmes"
])

# 1. ABA DO SIMULADOR (Tabela PRICE)
with aba_simulador:
    st.subheader("Simulação de Financiamento")
    v_imo = st.number_input("Valor do Imóvel (R$)", value=250000.0, step=1000.0)
    j_anual = st.number_input("Taxa de Juros Anual (%)", value=10.5)
    p_anos = st.slider("Prazo (Anos)", 1, 35, 20)
    
    sistema = KelvinSistema(v_imo, j_anual, p_anos)
    parcela = sistema.calcular_parcela()
    
    st.metric("Parcela Mensal Estimada", f"R$ {parcela:,.2f}")
    st.line_chart(sistema.dados_grafico())
    st.caption("Cálculo baseado no sistema de amortização PRICE.")

# 2. ABA DE ATENDIMENTO COM WHATSAPP
with aba_atendimento:
    st.subheader("Atendimento Rápido")
    nome_cliente = st.text_input("Nome do Cliente:")
    
    assinatura = f"\n\nAtenciosamente,\nKelvin Eiyng\nCRECI-SC 49891 F"
    
    frases = {
        "Boas vindas": f"Oi {nome_cliente}, vi que você chamou no Marketplace sobre o imóvel. Tudo bem? Como posso te ajudar?",
        "Vídeo do Imóvel": f"Olá {nome_cliente}, separei um vídeo desse imóvel para você ver os detalhes. Posso te enviar por aqui?",
        "Documentação": f"Oi {nome_cliente}, para avançarmos com a simulação bancária, você consegue me enviar sua renda bruta e CPF?"
    }
    
    escolha = st.selectbox("Selecione o modelo:", list(frases.keys()))
    mensagem_final = frases[escolha] + assinatura
    
    st.info(f"**Pré-visualização:**\n\n{mensagem_final}")
    
    # Formatação de link para WhatsApp
    link_wa = f"https://wa.me/?text={mensagem_final.replace(' ', '%20').replace('\n', '%0A')}"
    st.markdown(f"[📲 ENVIAR PARA O WHATSAPP]({link_wa})")

# 3. ABA DE AGENDA E ALERTAS
with aba_agenda:
    st.subheader("Gestão de Compromissos")
    
    with st.expander("➕ Novo Lembrete"):
        cli = st.text_input("Nome do Lead")
        h = st.time_input("Hora do Alarme")
        status = st.selectbox("Status:", [
            "🔴 URGENTE - Chamar agora", 
            "🔵 VISITA - Agendada", 
            "🟢 RETORNAR - Em aberto"
        ])
        if st.button("Salvar na Agenda"):
            st.session_state.agenda_contatos.append({
                "nome": cli, "hora": h, "cor": status, "avisado": False
            })
            st.success("Salvo!")

    # Lógica de verificação de horário para alarme visual
    hora_atual = datetime.now().time().strftime("%H:%M")
    for item in st.session_state.agenda_contatos:
        if item['hora'].strftime("%H:%M") == hora_atual and not item['avisado']:
            st.toast(f"🚨 HORA DE FALAR COM: {item['nome']}", icon="⏰")
            item['avisado'] = True

    # Exibição da lista de contatos
    for i in st.session_state.agenda_contatos:
        texto_item = f"{i['hora'].strftime('%H:%M')} - {i['nome']} ({i['cor']})"
        if "🔴" in i['cor']: st.error(texto_item)
        elif "🔵" in i['cor']: st.info(texto_item)
        else: st.success(texto_item)
