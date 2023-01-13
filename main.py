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
    print(produto['descricao'])
    print(produto['preco'])
    print(produto['id'])

def post_dados(product):
    requests.post("http://localhost:3000/produtos", json=product.__dict__)

def put_dados(id, product):
    requests.put(f"http://localhost:3000/produtos/{id}", json=product.__dict__)

if __name__ == '__main__':
    get_dados()
    post_dados(product.Product("Fruki", "Frukizao laranja", "7.5"))
    put_dados("4", product.Product("FrukiEDITED", "Frukizao laranjaEDITED", "7.6"))
    get_dados_id("4")