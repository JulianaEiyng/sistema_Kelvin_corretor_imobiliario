import streamlit as st
import pandas as pd
from datetime import datetime

# Estrutura principal do sistema de cálculos financeiros
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

# Configuração da interface e identidade visual
st.set_page_config(page_title="Kelvin Eiyng - Inteligência Imobiliária", layout="centered")

# Inicialização do estado da agenda para persistência de dados
if 'agenda_contatos' not in st.session_state:
    st.session_state.agenda_contatos = []

# Identificação Profissional no Cabeçalho
st.title("💼 Central Kelvin Pro")
st.markdown(f"**Corretor:** Kelvin Eiyng | **CRECI-SC:** 49891 F")
st.markdown("---")

# Navegação por abas funcionais
aba_simulador, aba_atendimento, aba_agenda = st.tabs([
    "📊 Simulador", "🚀 Mensagens Rápidas", "🗓️ Agenda & Alarmes"
])

# Interface do Simulador Financeiro (Tabela PRICE)
with aba_simulador:
    st.subheader("Simulação de Financiamento")
    v_imo = st.number_input("Valor do Imóvel (R$)", value=250000.0, step=1000.0)
    j_anual = st.number_input("Taxa de Juros Anual (%)", value=10.5)
    p_anos = st.slider("Prazo (Anos)", 1, 35, 20)
    
    sistema = KelvinSistema(v_imo, j_anual, p_anos)
    parcela = sistema.calcular_parcela()
    
    st.metric("Parcela Mensal Estimada", f"R$ {parcela:,.2f}")
    st.line_chart(sistema.dados_grafico())
    st.caption("Nota: Valores simulados com base na tabela PRICE.")

# Interface de Atendimento Rápido com Assinatura Automática
with aba_atendimento:
    st.subheader("Gestão de Mensagens WhatsApp")
    nome_cliente = st.text_input("Nome do Cliente:")
    
    # Assinatura padrão para todas as mensagens
    assinatura = f"\n\nAtenciosamente,\nKelvin Eiyng\nCRECI-SC 49891 F"
    
    frases = {
        "Boas vindas": f"Oi {nome_cliente}, vi que você chamou no Marketplace sobre o imóvel. Tudo bem? Como posso te ajudar?",
        "Vídeo do Imóvel": f"Olá {nome_cliente}, separei um vídeo desse imóvel para você ver os detalhes. Posso te enviar por aqui?",
        "Documentação": f"Oi {nome_cliente}, para avançarmos com a simulação bancária, você consegue me enviar sua renda bruta e CPF?"
    }
    
    escolha = st.selectbox("Selecione o modelo de mensagem:", list(frases.keys()))
    mensagem_final = frases[escolha] + assinatura
    
    st.info(f"**Visualização da Mensagem:**\n\n{mensagem_final}")
    
    # Formatação de link para abertura direta no WhatsApp
    link_wa = f"https://wa.me/?text={mensagem_final.replace(' ', '%20').replace('\n', '%0A')}"
    st.markdown(f"[📲 ENVIAR PARA O WHATSAPP]({link_wa})")

# Gestão de compromissos e sistema de monitoramento de horários
with aba_agenda:
    st.subheader("Agenda de Leads e Retornos")
    
    with st.expander("➕ Agendar Novo Compromisso"):
        cli = st.text_input("Nome do Lead")
        h = st.time_input("Horário do Alarme")
        status = st.selectbox("Prioridade Visual:", [
            "🔴 URGENTE - Retorno Imediato", 
            "🔵 VISITA - Agendada", 
            "🟢 RETORNAR - Em aberto"
        ])
        if st.button("Salvar Compromisso"):
            st.session_state.agenda_contatos.append({
                "nome": cli, "hora": h, "cor": status, "avisado": False
            })
            st.success("Lembrete salvo com sucesso!")

    # Monitoramento de horário para disparo de alertas visuais
    hora_atual = datetime.now().time().strftime("%H:%M")
    for item in st.session_state.agenda_contatos:
        if item['hora'].strftime("%H:%M") == hora_atual and not item['avisado']:
            st.toast(f"⏰ HORA DE FALAR COM: {item['nome']}", icon="🚨")
            item['avisado'] = True

    # Renderização da lista de Leads categorizada por cores
    for i in st.session_state.agenda_contatos:
        texto_item = f"{i['hora'].strftime('%H:%M')} - {i['nome']} ({i['cor']})"
        if "🔴" in i['cor']: st.error(texto_item)
        elif "🔵" in i['cor']: st.info(texto_item)
        else: st.success(texto_item)
