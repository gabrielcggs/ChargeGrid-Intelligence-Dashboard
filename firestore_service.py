import os
import requests
from dotenv import load_dotenv
from auth_service import get_anonymous_token

load_dotenv()
PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")

def get_firestore_headers():
    token = get_anonymous_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def salvar_sessao_recarga(*args, **kwargs):
    """Suporta chamadas com dicionário ou múltiplos argumentos posicionais/nomeados do Totem."""
    dados_sessao = {}
    
    if args and isinstance(args[0], dict):
        dados_sessao = args[0]
    elif args:
        param_names = ["stationId", "energyKwh", "timestamp", "modelo", "kwh", "porcentagem"]
        for i, val in enumerate(args):
            if i < len(param_names):
                dados_sessao[param_names[i]] = val
                
    for k, v in kwargs.items():
        dados_sessao[k] = v

    url = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/sessoes"
    headers = get_firestore_headers()
    
    fields = {}
    for key, value in dados_sessao.items():
        if isinstance(value, (int, float)):
            fields[key] = {"doubleValue": float(value)}
        else:
            fields[key] = {"stringValue": str(value)}

    body = {"fields": fields}
    
    response = requests.post(url, headers=headers, json=body)
    return response.json()

def listar_sessoes_recarga(limite=None, **kwargs):
    """Busca as sessões registradas no Firestore e garante o campo 'criado_em' para o dashboard."""
    url = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/sessoes"
    headers = get_firestore_headers()
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        documentos = data.get("documents", [])
        resultado = []
        for doc in documentos:
            fields = doc.get("fields", {})
            doc_id = doc.get("name", "").split("/")[-1]
            
            item = {"id": doc_id}
            for k, v in fields.items():
                if "stringValue" in v:
                    item[k] = v["stringValue"]
                elif "doubleValue" in v:
                    item[k] = v["doubleValue"]
                elif "integerValue" in v:
                    item[k] = int(v["integerValue"])
            
            # Garante a existência do campo 'criado_em' para evitar quebras no dashboard
            if "criado_em" not in item:
                item["criado_em"] = item.get("timestamp", "2026-08-31 00:00:00")
                
            resultado.append(item)
            
        if limite and isinstance(limite, int):
            resultado = resultado[:limite]
            
        return resultado
    return []

def ultima_sessao_recarga():
    """Retorna os dados da última sessão no formato exato que o calculos_totem.py espera."""
    sessoes = listar_sessoes_recarga()
    if sessoes:
        return sessoes[-1]
    
    return {
        "kwh": 50,
        "porcentagem": 20,
        "stationId": "Totem-01",
        "modelo": "Padrão"
    }