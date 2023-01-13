import requests
import json
import product

def get_dados():
    request = requests.get("http://localhost:3000/produtos")
    produtos = json.loads(request.content)
    for produto in produtos:
        print(produto)

def get_dados_id(id):
    request = requests.get(f"http://localhost:3000/produtos/{id}")
    produto = json.loads(request.content)
    print(produto['nome'])

def post_dados(product):
    requests.post("http://localhost:3000/produtos", json=product.__dict__)

if __name__ == '__main__':
    post_dados(product.Product("Fruki", "Frukizao laranja", "7.5"))
    get_dados()
    get_dados_id("4")