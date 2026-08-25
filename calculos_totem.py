from firestore_service import ultima_sessao_recarga

ultimo = ultima_sessao_recarga()

if ultimo is None:
    raise RuntimeError(
        "Nenhuma sessão de recarga encontrada no Firestore ainda. "
        "Preencha o formulário do Totem antes de abrir o painel de informações."
    )

ener_consumida = int(ultimo["kwh"]) - int(ultimo["kwh"]) * (int(ultimo["porcentagem"]) / 100)

tempo = ener_consumida / 50

tempo_h = int(ener_consumida / 50)

tempo_m = (tempo - tempo_h) * 60

valor_total = ener_consumida * 2 + 1.80