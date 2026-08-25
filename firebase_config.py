"""
firebase_config.py

Ponto único de configuração e conexão com o Firebase.

Por que esse arquivo existe separado:
- O projeto tem DOIS pontos de entrada Python diferentes (dashboard.py, que roda
  via Streamlit, e Totem.py, que roda como app desktop via customtkinter).
- Ambos precisam falar com o mesmo Firestore, com as mesmas credenciais.
- Centralizando a conexão aqui, qualquer um dos dois só precisa fazer:
      from firebase_config import get_db

Configuração necessária (ver FIREBASE_SETUP.md):
- Um arquivo .env na raiz do projeto com:
      FIREBASE_SERVICE_ACCOUNT_PATH=firebase_service_account.json
      FIREBASE_WEB_API_KEY=coloque_aqui_a_chave_web_do_projeto
- O arquivo JSON da conta de serviço (baixado do console do Firebase),
  salvo no caminho apontado por FIREBASE_SERVICE_ACCOUNT_PATH.

IMPORTANTE: nunca commitar o .env nem o JSON da conta de serviço no GitHub
(ambos já estão listados no .gitignore deste projeto).
"""

import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

_db = None  # cache simples em memória do processo


def get_db():
    """
    Retorna um cliente Firestore já autenticado, inicializando o app
    do Firebase Admin SDK na primeira chamada (e reaproveitando nas seguintes).
    """
    global _db

    if _db is not None:
        return _db

    if not firebase_admin._apps:
        cred_path = os.getenv(
            "FIREBASE_SERVICE_ACCOUNT_PATH", "firebase_service_account.json"
        )

        if not os.path.exists(cred_path):
            raise FileNotFoundError(
                f"Não encontrei o arquivo de credenciais do Firebase em '{cred_path}'.\n"
                "Veja o FIREBASE_SETUP.md para saber como gerar e configurar esse arquivo."
            )

        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

    _db = firestore.client()
    return _db
