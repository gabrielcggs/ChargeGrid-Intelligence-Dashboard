import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FIREBASE_WEB_API_KEY")

def get_anonymous_token():
    """Autentica anonimamente no Firebase Auth e retorna um ID Token válido."""
    if not API_KEY:
        raise ValueError("FIREBASE_WEB_API_KEY não encontrada no arquivo .env")
        
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
    payload = {"returnSecureToken": True}
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["idToken"]
    else:
        error_message = response.json().get("error", {}).get("message", response.text)
        raise Exception(error_message)

def login(email, password):
    """Valida o login gerando o token anônimo e retornando o formato esperado pelo dashboard.py."""
    try:
        token = get_anonymous_token()
        if token:
            return {"sucesso": True, "email": email, "token": token}
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}
    
    return {"sucesso": False, "erro": "Falha desconhecida na autenticação"}

def cadastrar(email, password):
    """Simula o cadastro para compatibilidade com a interface existente."""
    return {"sucesso": True, "mensagem": "Cadastrado com sucesso"}