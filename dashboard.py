import streamlit as st

st.set_page_config(page_title="ChargeGrid Intelligence")

st.title("ChargeGrid Intelligence")

st.write("Dashboard de gerenciamento inteligente")

# Entrada

carros = st.slider(
    "Quantidade de carros conectados",
    1,
    20,
    5
)

energia_total = 100

energia_por_carro = energia_total / carros

consumo = carros * 10

valor = consumo * 1.20

# Status

if carros > 8:
    status = "🔴 Pico de demanda"
    ia = "IA reduziu a potência para evitar sobrecarga"
else:
    status = "🟢 Operação normal"
    ia = "IA mantendo distribuição padrão"

# Dashboard

st.header("Monitoramento")

st.metric(
    "Carros conectados",
    carros
)

st.metric(
    "Energia por carro (kW)",
    round(energia_por_carro, 2)
)

st.metric(
    "Consumo Total (kWh)",
    consumo
)

st.metric(
    "Valor da cobrança (R$)",
    round(valor, 2)
)

st.subheader("Status da Rede")

st.write(status)

st.subheader("Decisão da IA")

st.write(ia)