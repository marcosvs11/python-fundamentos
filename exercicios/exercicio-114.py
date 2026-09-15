from urllib.request import Request, urlopen
from urllib.error import URLError

pedido = Request('http://www.pudim.com.br',  headers={'User-Agent': 'Mozilla/5.0'})

try:
    resposta = urlopen(pedido)

except URLError:
    print('O site desejado não está disponível!')
else:
    print('Acesso com sucesso!')
