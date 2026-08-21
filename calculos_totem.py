import json

with open("dados_recarga.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

ultimo = dados[-1]


ener_consumida = int(ultimo["kwh"]) - int(ultimo["kwh"]) * (int(ultimo["porcentagem"]) / 100)

tempo = ener_consumida / 50

tempo_h = int(ener_consumida / 50)

tempo_m = (tempo - tempo_h) * 60

valor_total = ener_consumida * 2 + 1.80