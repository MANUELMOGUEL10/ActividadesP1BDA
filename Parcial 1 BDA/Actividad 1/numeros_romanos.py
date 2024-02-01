import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.twinkl.co.uk/teaching-wiki/numeros-en-ingles'

response = requests.get(url)

if response.status_code == 200:

  soup = BeautifulSoup(response.text,'html.parser')

  table = soup.find('table',{'bgcolor':'white'})

  rows = table.find_all('tr')

  numeros_romanos = []

  for row in rows[1:]:
    cols = row.find_all('td')

    if len(cols) == 4:
      arabe_number = cols[0].text.strip()
      cardinal_number = cols[1].text.strip()
      ordinal_number = cols[1].text.strip()
      romano_number = cols[1].text.strip()
      numeros_romanos.append({'Arabes':arabe_number, 'Cardinales':cardinal_number, 'ordinales':ordinal_number, 'Romanos':romano_number})

  json_data = json.dumps(numeros_romanos, indent=4, ensure_ascii=False)

  with open('numeros_romanos.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

  print("Datos extraidos y guardados en numeros_romanos.json")

else:

  print("error al conectarse a la web")