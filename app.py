import streamlit as st
import urllib.parse

# Configuração da Identidade do Corretor e Empresa
st.set_page_config(page_title="Kelvin Eiyng - Corretor", layout="wide")

# Estilo para destacar o nome e o CRECI
st.markdown("""
    <style>
    .nome-destaque { font-size: 42px; font-weight: bold; color: #004aad; margin-bottom: 0px; }
    .creci-destaque { font-size: 24px; color: #555; margin-top: -10px; font-weight: bold; }
    .villa-terra { font-size: 18px; color: #888; margin-top: 5px; }
    .stButton>button { width: 100%; height: 50px; border-radius: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho com Hierarquia Visual (Nome > CRECI > Villa Terra)
st.markdown('<p class="nome-destaque">Kelvin Eiyng</p>', unsafe_allow_html=True)
st.markdown('<p class="creci-destaque">CRECI-SC 49891 F</p>', unsafe_allow_html=True)
st.markdown('<p class="villa-terra">Parceiro Imobiliária Villa Terra</p>', unsafe_allow_html=True)
st.markdown(f"📱 WhatsApp: (48) 98461-0091")

# Redes Sociais na lateral (com base nas suas fotos)
st.sidebar.title("🔗 Minhas Redes")
st.sidebar.markdown("[Instagram Profissional](https://www.instagram.com/kelvineiyngcorretor/)")
st.sidebar.markdown("[Facebook Marketplace](https://www.facebook.com/kelvin.eiyng)")

st.markdown("---")

# Menu de navegação
menu = st.sidebar.radio("Navegação", ["Secretária Marketplace", "Calculadora de Comissão"])

if menu == "Secretária Marketplace":
    st.subheader("📲 Resposta Rápida (Secretária Digital)")
    
    nome_cliente = st.text_input("Nome do Cliente")
    fone_cliente = st.text_input("WhatsApp do Cliente (DDD + Número)", placeholder="48984610000")
    
    msg_tipo = st.selectbox("O que você quer enviar?", [
        "Apresentação Pessoal (Mkt Place)",
        "Agendar Visita (Villa Terra)",
        "Localização do Escritório"
    ])
    
    # Assinatura com o Kelvin em destaque
    assinatura = "\n\n---\n*Kelvin Eiyng*\nCRECI-SC 49891 F\n(Imobiliária Villa Terra)"
    
    msgs = {
        "Apresentação Pessoal (Mkt Place)": f"Olá {nome_cliente}! Sou o Kelvin Eiyng, vi seu interesse no imóvel anunciado. Gostaria de receber mais detalhes agora?{assinatura}",
        "Agendar Visita (Villa Terra)": f"Oi {nome_cliente}! Vamos agendar uma visita para você conhecer esse imóvel pessoalmente? Qual horário fica melhor?{assinatura}",
        "Localização do Escritório": f"Oi {nome_cliente}! Nosso escritório fica em Criciúma. Se quiser tomar um café e conversar, estou à disposição!{assinatura}"
    }
    
    texto_final = msgs[msg_tipo]
    st.info(f"Prévia da Mensagem:\n\n{texto_final}")
    
    if st.button("🚀 ENVIAR WHATSAPP AGORA"):
        if fone_cliente:
            fone_limpo = "".join(filter(str.isdigit, fone_cliente))
            link = f"https://wa.me/55{fone_limpo}?text={urllib.parse.quote(texto_final)}"
            st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none;"><button style="width:100%; background-color:#25D366; color:white; border:none; padding:15px; border-radius:10px; cursor:pointer;">ABRIR WHATSAPP DO KELVIN</button></a>', unsafe_allow_html=True)
        else:
            st.error("Coloque o WhatsApp do cliente.")

elif menu == "Calculadora de Comissão":
    st.subheader("💰 Simulação de Lucro")
    valor = st.number_input("Valor da Venda (R$)", value=300000)
    comissao = st.slider("Sua % de Comissão", 1.0, 6.0, 2.0)
    
    resultado = valor * (comissao / 100)
    st.metric("Sua Comissão Estimada", f"R$ {resultado:,.2f}")