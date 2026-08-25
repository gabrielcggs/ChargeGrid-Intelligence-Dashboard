import streamlit as st
import pandas as pd

from auth_service import login, cadastrar
from firestore_service import listar_sessoes_recarga

st.set_page_config(page_title="ChargeGrid Intelligence", layout="wide")

# ==========================================================
#                     Controle de sessão / login
# ==========================================================

if "usuario" not in st.session_state:
    st.session_state.usuario = None


def tela_login_e_cadastro():
    st.title("ChargeGrid Intelligence")
    st.caption("Acesso restrito a operadores")

    aba_login, aba_cadastro = st.tabs(["Entrar", "Criar conta"])

    with aba_login:
        with st.form("form_login"):
            email = st.text_input("E-mail")
            senha = st.text_input("Senha", type="password")
            entrar = st.form_submit_button("Entrar")

        if entrar:
            resultado = login(email, senha)
            if resultado["sucesso"]:
                st.session_state.usuario = resultado
                st.rerun()
            else:
                st.error(f"Falha no login: {resultado['erro']}")

    with aba_cadastro:
        st.caption("Crie seu acesso de operador — não precisa mexer no Firebase.")

        with st.form("form_cadastro"):
            novo_email = st.text_input("E-mail", key="cadastro_email")
            nova_senha = st.text_input(
                "Senha (mínimo 6 caracteres)", type="password", key="cadastro_senha"
            )
            confirmar_senha = st.text_input(
                "Confirme a senha", type="password", key="cadastro_confirmar"
            )
            criar_conta = st.form_submit_button("Criar conta")

        if criar_conta:
            if nova_senha != confirmar_senha:
                st.error("As senhas não coincidem.")
            elif len(nova_senha) < 6:
                st.error("A senha precisa ter pelo menos 6 caracteres.")
            else:
                resultado = cadastrar(novo_email, nova_senha)
                if resultado["sucesso"]:
                    st.success("Conta criada com sucesso! Agora faça login na aba \"Entrar\".")
                else:
                    st.error(f"Não foi possível criar a conta: {resultado['erro']}")


if st.session_state.usuario is None:
    tela_login_e_cadastro()
    st.stop()

# ==========================================================
#                     Dashboard (usuário logado)
# ==========================================================

with st.sidebar:
    st.write(f"👤 Logado como **{st.session_state.usuario['email']}**")
    if st.button("Sair"):
        st.session_state.usuario = None
        st.rerun()

st.title("ChargeGrid Intelligence")
st.write("Dashboard de gerenciamento inteligente")

# --- Simulação de operação (mantida do protótipo original) ---

carros = st.slider("Quantidade de carros conectados", 1, 20, 5)

energia_total = 100
energia_por_carro = energia_total / carros
consumo = carros * 10
valor = consumo * 1.20

if carros > 8:
    status = "🔴 Pico de demanda"
    ia = "IA reduziu a potência para evitar sobrecarga"
else:
    status = "🟢 Operação normal"
    ia = "IA mantendo distribuição padrão"

st.header("Monitoramento")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Carros conectados", carros)
col2.metric("Energia por carro (kW)", round(energia_por_carro, 2))
col3.metric("Consumo Total (kWh)", consumo)
col4.metric("Valor da cobrança (R$)", round(valor, 2))

st.subheader("Status da Rede")
st.write(status)

st.subheader("Decisão da IA")
st.write(ia)

# --- Histórico real, vindo do Firestore (alimentado pelo Totem) ---

st.divider()
st.header("Histórico de Sessões de Recarga")
st.caption("Dados reais gravados pelo Totem e persistidos no Firestore.")

try:
    sessoes = listar_sessoes_recarga(limite=50)
except Exception as e:
    sessoes = []
    st.warning(f"Não foi possível carregar o histórico do Firestore agora: {e}")

if sessoes:
    df = pd.DataFrame(sessoes)
    colunas_ordenadas = [c for c in ["criado_em", "modelo", "porcentagem", "kwh"] if c in df.columns]
    st.dataframe(df[colunas_ordenadas], use_container_width=True)
else:
    st.info("Nenhuma sessão registrada ainda. Use o Totem para registrar uma recarga.")
