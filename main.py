import requests
import json


def get_dados():
    request = requests.get("http://localhost:3000/produtos")
    product = json.loads(request.content)
    print(product)  # pegando todos itens da lista

def get_dados_id(id):
    request = requests.get(f"viacep.com.br/ws/01001000/json/")
    product = json.loads(request.content)
    print(product[4]['nome'])  # pegando so o nome do segundo item da lista (Coca cola 350ml)


# pegando dados por id
if __name__ == '__main__':
    get_dados()
    get_dados_id()
