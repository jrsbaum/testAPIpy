import requests

def get_dados():
    request = requests.get("http://localhost:3000/produtos")
    print(request.content)

if __name__ == '__main__':
    get_dados()