import requests
from bs4 import BeautifulSoup

print('Bem vindo ao Google Searcher!\n')

search_string = input('Digite um termo para buscar no Google: ')
search_params = {'q': search_string}


http_request = requests.get('https://www.google.com/search',params=search_params)

results_page = BeautifulSoup(http_request.text, "html.parser")


h3_title_list = results_page.find_all('h3')

print('\nResultados obtidos:\n')


for h3 in h3_title_list:
    title = h3.getText()
    

    print('     Título:',title)
    print()
