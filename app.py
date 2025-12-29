import streamlit as st
import urllib.parse

# Configuração da página e Estilo Villa Terra
st.set_page_config(page_title="Kelvin Eiyng - Consultor Imobiliário", page_icon="🏠")

st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; background-color: #1d3557; color: white; border-radius: 10px; height: 3em; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho com Autoridade
st.title("💼 Central de Vendas - Kelvin Eiyng")
st.caption("Parceiro Imobiliário Villa Terra | CRECI-SC 49891 F")

aba1, aba2 = st.tabs(["🚀 Respostas Rápidas", "🧮 Simulador de Parcelas"])

with aba1:
    st.subheader("Gatilhos de Conversa (Curtos)")
    nome_cliente = st.text_input("Nome do Lead")
    fone_cliente = st.text_input("WhatsApp do Lead (ex: 48984610091)")
    
    msg_tipo = st.selectbox("O que enviar?", [
        "Isca 1: Pergunta sobre Vídeo",
        "Isca 2: Agendar Visita",
        "Isca 3: Follow-up (Retorno)"
    ])

    textos = {
        "Isca 1: Pergunta sobre Vídeo": f"Oi {nome_cliente}, vi seu interesse no imóvel. Você quer que eu te mande o vídeo completo dele por aqui?",
        "Isca 2: Agendar Visita": f"Fala {nome_cliente}! Gostou das fotos? Tenho um horário livre para te mostrar ele amanhã. Qual horário fica melhor para você?",
        "Isca 3: Follow-up (Retorno)": f"Oi {nome_cliente}, tudo bem? Só passando para saber se ainda tem interesse naquele imóvel ou se quer que eu te mande outras opções no mesmo perfil."
    }
    
    msg_final = textos[msg_tipo]
    st.info(msg_final)

    if st.button("Enviar para o WhatsApp"):
        if fone_cliente:
            texto_url = urllib.parse.quote(msg_final)
            link = f"https://wa.me/55{fone_cliente}?text={texto_url}"
            st.markdown(f'<a href="{link}" target="_blank">Abrir conversa agora</a>', unsafe_allow_html=True)
        else:
            st.error("Coloque o número do cliente!")

with aba2:
    st.subheader("Simulação Rápida (Para usar na visita)")
    valor_imovel = st.number_input("Valor do Imóvel (R$)", value=300000)
    entrada = st.number_input("Entrada (R$)", value=60000)
    prazo_anos = st.slider("Prazo (Anos)", 10, 35, 30)
    
    saldo = valor_imovel - entrada
    parcela_aprox = (saldo / (prazo_anos * 12)) * 1.6 # Estimativa com juros médios
    
    st.metric("Parcela Estimada (Médio)", f"R$ {parcela_aprox:,.2f}")
    st.warning("Atenção: Valores aproximados para base de negociação.")

st.divider()
st.write("Dica: Adicione este site à tela inicial do seu celular para usar como um App!")
