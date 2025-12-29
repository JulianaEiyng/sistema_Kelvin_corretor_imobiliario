import streamlit as st
import urllib.parse

# Configuração e Identidade Visual Villa Terra
st.set_page_config(page_title="Kelvin Eiyng - Villa Terra", page_icon="🏠")

# CSS para mudar as cores para um tom azul escuro e dourado (profissional)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stButton>button { width: 100%; background-color: #0c2461; color: white; border-radius: 8px; font-weight: bold; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #f1f2f6; border-radius: 5px 5px 0px 0px; padding: 10px; }
    .instruction { font-size: 0.85rem; color: #636e72; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

# Título e Logo
st.title("🏠 Central do Corretor")
st.subheader("Kelvin Eiyng | CRECI-SC 49891 F")
st.markdown("---")

aba1, aba2 = st.tabs(["💬 Mensagens Isca", "📊 Simulador de Venda"])

with aba1:
    st.markdown("### 🚀 Enviar Mensagem Rápida")
    st.markdown('<p class="instruction">Use estas frases curtas para fazer o cliente responder mais rápido.</p>', unsafe_allow_html=True)
    
    nome_cliente = st.text_input("Nome do Cliente", placeholder="Ex: João")
    fone_cliente = st.text_input("WhatsApp com DDD", placeholder="Ex: 48984610091")
    
    st.markdown('<p class="instruction">Escolha o objetivo da conversa:</p>', unsafe_allow_html=True)
    msg_tipo = st.selectbox("", [
        "Saber se quer ver o vídeo do imóvel",
        "Convidar para visita amanhã",
        "Retomar contato (Follow-up)"
    ])

    textos = {
        "Saber se quer ver o vídeo do imóvel": f"Oi {nome_cliente}, vi seu interesse no imóvel. Quer que eu te mande o vídeo completo dele agora?",
        "Convidar para visita amanhã": f"Fala {nome_cliente}! Gostou das fotos? Tenho um horário livre amanhã. Que horas fica bom para você ver o imóvel?",
        "Retomar contato (Follow-up)": f"Oi {nome_cliente}, tudo bem? Só passando para saber se ainda tem interesse ou se quer outras opções no mesmo perfil."
    }
    
    msg_final = textos[msg_tipo]
    st.code(msg_final, language=None)

    if st.button("🚀 ENVIAR PELO WHATSAPP"):
        if fone_cliente:
            texto_url = urllib.parse.quote(msg_final)
            link = f"https://wa.me/55{fone_cliente}?text={texto_url}"
            st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none;"><button style="width:100%; background-color:#25d366; color:white; border:none; padding:10px; border-radius:8px; cursor:pointer;">Confirmar e Abrir WhatsApp</button></a>', unsafe_allow_html=True)
        else:
            st.error("Por favor, digite o número do cliente.")

with aba2:
    st.markdown("### 🧮 Simulação para o Cliente")
    st.markdown('<p class="instruction">Use isto durante a visita para dar uma estimativa de parcelas.</p>', unsafe_allow_html=True)
    
    v_imovel = st.number_input("Valor do Imóvel (R$)", value=350000, step=50000)
    v_entrada = st.number_input("Entrada disponível (R$)", value=70000, step=10000)
    
    saldo = v_imovel - v_entrada
    st.write(f"**Valor a financiar:** R$ {saldo:,.2f}")
    
    prazo = st.select_slider("Prazo (Anos)", options=[10, 15, 20, 25, 30, 35], value=30)
    
    # Cálculo simples de prestação (Price aproximada)
    juros = 0.009 # Aprox 10.5% ao ano
    n = prazo * 12
    parcela = saldo * ( (juros * (1 + juros)**n) / ((1 + juros)**n - 1) )
    
    st.metric("Parcela Estimada", f"R$ {parcela:,.2f}")
    st.markdown('<p class="instruction">*Valores baseados em taxas médias de mercado. Sujeito a análise bancária.</p>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Sistema desenvolvido para Kelvin Eiyng - Villa Terra")
   
            
