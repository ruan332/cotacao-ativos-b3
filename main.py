import requests
from bs4 import BeautifulSoup

# URL da página da B3 com as cotações
url = 'https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/'

# Fazendo uma requisição GET para a URL
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
  # Convertendo o conteúdo da página em um objeto BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')

  # Procurando todas as cotações na página
  cotacoes = soup.find_all('tr', class_='odd') + soup.find_all('tr', class_='even')

  # Imprimindo informações sobre cada cotação encontrada
  for cotacao in cotacoes:
    ativo = cotacao.find('a').text
    ultimo_preco = cotacao.find('td', class_='last').text
    print(f'Ativo: {ativo} | Último preço: {ultimo_preco}')
else:
  print('Erro ao acessar o site')
