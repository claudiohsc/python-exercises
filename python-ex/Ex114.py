import requests

response = requests.get('http://pudim.com.br')
try:
    response.status_code
except:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site.')