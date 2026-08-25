

import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

_db = None  

def get_db():
    
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
