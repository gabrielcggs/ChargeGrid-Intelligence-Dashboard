
from datetime import datetime, timezone
from firebase_config import get_db

_COLECAO = "sessoes_recarga"


def salvar_sessao_recarga(modelo: str, porcentagem, kwh) -> str:

    db = get_db()

    novo_registro = {
        "modelo": modelo,
        "porcentagem": porcentagem,
        "kwh": kwh,
        "criado_em": datetime.now(timezone.utc).isoformat(),
    }

    _, doc_ref = db.collection(_COLECAO).add(novo_registro)
    return doc_ref.id



    db = get_db()

    docs = (
        db.collection(_COLECAO)
        .order_by("criado_em", direction="DESCENDING")
        .limit(limite)
        .stream()
    )

    resultado = []
    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        resultado.append(item)
    return resultado


def ultima_sessao_recarga() -> dict | None:

    sessoes = listar_sessoes_recarga(limite=1)
    return sessoes[0] if sessoes else None
