import requests
from bs4 import BeautifulSoup

URL = 'https://es.wikipedia.org/wiki/Anexo:M%C3%A1ximos_anotadores_de_triples_de_la_historia_de_la_NBA'

def get_top_n_majors_three_pointers_nba(n):
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', attrs={'style': "font-size: 99%;"})

    if not table:
        raise Exception("No hay tabla")

    table_rows = table.find_all('tr')

    table_data = []
    for row in table_rows[1:6]:
        table_data.append([data for data in row.text.split('\n') if data != ''])

    for row in range(len(table_data)):
        splited = table_data[row][1].split(' ')
        if len(splited) > 2:
            splited = splited[len(splited)//2:]
            splited[0] = splited[0][len(splited[0])//2:]
        splited[-1] = splited[-1][:len(splited[-1])-1]
        table_data[row][1] = ' '.join(splited)     


    relevant_data = [[data[0],data[1],data[-1]] for data in table_data]
    return relevant_data
