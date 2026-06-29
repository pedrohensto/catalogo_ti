## P2 CSI-22 -- Catalogo de Prestadores de Servico TI
## Pedro Henrique Moreira
## Lucas Ulrich
## ====================================================

# esse modulo vai fazer o preenchimento automatico do endereco via CEP
# do site: https://viacep.com.br/
# exemplo:
#   URL: viacep.com.br/ws/01001000/json/
#
#
#     {
#       "cep": "01001-000",
#       "logradouro": "Praça da Sé",
#       "complemento": "lado ímpar",
#       "unidade": "",
#       "bairro": "Sé",
#       "localidade": "São Paulo",
#       "uf": "SP",
#       "estado": "São Paulo",
#       "regiao": "Sudeste",
#       "ibge": "3550308",
#       "gia": "1004",
#       "ddd": "11",
#       "siafi": "7107"
#     }
#
#     vamos chamar isso via urlib.request
#
import urllib.request
import json


def consultar_cep(cep):
    if len(cep) != 8:
        raise ValueError("CEP deve ter 8 digitos.")
    url = "https://viacep.com.br/ws/" + cep + "/json/"
    try:
        with urllib.request.urlopen(url, timeout=5) as resposta:
            texto = resposta.read()
    except Exception:
        raise ValueError("Nao foi possivel consultar o CEP (verifique a internet).")
    dados = json.loads(texto)
    # viacep devolve erro: true no dict
    if dados.get("erro"):
        raise ValueError("CEP nao encontrado.")
    return {
        "rua": dados.get("logradouro", ""),
        "complemento": dados.get("complemento", ""),
        "bairro": dados.get("bairro", ""),
        "cidade": dados.get("localidade", ""),
        "uf": dados.get("uf", ""),
    }

