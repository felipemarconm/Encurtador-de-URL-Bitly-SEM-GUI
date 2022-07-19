# Rode o programa duas vezes seguidas para obter a URL encurtada :)

import requests

# Credenciais da conta Bitly
username = "nome_usuário" # Nome de úsuario
password = "senha" # Senha da conta

# Obter o token de acesso
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))

if auth_res.status_code == 200: # Se a resposta for OK, recebe o token de acesso
    access_token = auth_res.content.decode()
    print("* Obtive o token de acesso:", access_token)
else:
    print("* Não obtive o token de acesso, saindo...")
    exit()

# Request headers com autorização
headers = {"Authorization": f"Bearer {access_token}"}

# Obter o UID do grupo associado a conta
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)

if groups_res.status_code == 200: # Se a resposta for OK, recebe a GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("* Não foi possível obter o GUID, saindo...")
    exit()

url = "https://youtube.com" # Aqui deve ser inserido a URL a ser encurtada.
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers) # Faz o POST request para obter a URL inserida abreviada.

if shorten_res.status_code == 200: # Se a resposta for OK, recebe a URL encurtada.
    link = shorten_res.json().get("link")
    print("URL Encurtada:", link)