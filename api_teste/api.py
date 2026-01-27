# Busca dados climaticos de determinado pais, usando weatherAPi 
import requests
import pprint

api_key = "SUA_CHAVE_API"
link_api =  "http://api.weatherapi.com/v1/current.json"

parametros = {
    "Key": api_key,
    "q": "Salvador",
    "lang": "pt-BR"
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint.pprint(dados_requisicao)
    temp = dados_requisicao['current']['temp_c']
    condicao = dados_requisicao['current']['condition']['text']
    print(temp)
    print(condicao)
else:
    print("Erro na requisição:", resposta.status_code)


# status code 200 = sucesso
# status code 300 = redirecionamento
# status code 400 = erro na requisição
# status code 401 = não autorizado
# status code 404 = não encontrado
# status code 500 = erro no servidor
    