import os
from dotenv import load_dotenv
from auth_service import get_anonymous_token

load_dotenv()

PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")

def get_firestore_headers():
    """Retorna os headers HTTP necessários para interagir com o Firestore de forma segura."""
    token = get_anonymous_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def get_project_id():
    return PROJECT_ID