import os
import requests
from dotenv import load_dotenv

load_dotenv()

_FIREBASE_WEB_API_KEY = os.getenv("FIREBASE_WEB_API_KEY")

_SIGN_IN_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
_SIGN_UP_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"

_MENSAGENS_ERRO = {
    "EMAIL_NOT_FOUND": "E-mail não cadastrado.",
    "INVALID_PASSWORD": "Senha incorreta.",
    "INVALID_LOGIN_CREDENTIALS": "E-mail ou senha inválidos.",
    "USER_DISABLED": "Este usuário foi desativado.",
    "EMAIL_EXISTS": "Já existe uma conta com esse e-mail.",
    "WEAK_PASSWORD": "A senha precisa ter pelo menos 6 caracteres.",
}


def _checar_api_key():
    if not _FIREBASE_WEB_API_KEY:
        raise ValueError(
            "FIREBASE_WEB_API_KEY não encontrada. Configure o arquivo .env "
            "conforme o FIREBASE_SETUP.md."
        )


def login(email: str, senha: str) -> dict:

    _checar_api_key()

    payload = {"email": email, "password": senha, "returnSecureToken": True}
    params = {"key": _FIREBASE_WEB_API_KEY}

    try:
        resposta = requests.post(_SIGN_IN_URL, params=params, json=payload, timeout=10)
        dados = resposta.json()
    except requests.RequestException as e:
        return {"sucesso": False, "erro": f"Falha de conexão com o Firebase: {e}"}

    if resposta.status_code == 200:
        return {
            "sucesso": True,
            "email": dados["email"],
            "uid": dados["localId"],
            "token": dados["idToken"],
        }

    codigo_erro = dados.get("error", {}).get("message", "ERRO_DESCONHECIDO")
    return {"sucesso": False, "erro": _MENSAGENS_ERRO.get(codigo_erro, codigo_erro)}


def cadastrar(email: str, senha: str) -> dict:
    
    _checar_api_key()

    payload = {"email": email, "password": senha, "returnSecureToken": True}
    params = {"key": _FIREBASE_WEB_API_KEY}

    try:
        resposta = requests.post(_SIGN_UP_URL, params=params, json=payload, timeout=10)
        dados = resposta.json()
    except requests.RequestException as e:
        return {"sucesso": False, "erro": f"Falha de conexão com o Firebase: {e}"}

    if resposta.status_code == 200:
        return {"sucesso": True, "email": dados["email"], "uid": dados["localId"]}

    codigo_erro = dados.get("error", {}).get("message", "ERRO_DESCONHECIDO")
    return {"sucesso": False, "erro": _MENSAGENS_ERRO.get(codigo_erro, codigo_erro)}
