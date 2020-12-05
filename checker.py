import requests
from bs4 import BeautifulSoup

def get_availablity(url):
  soup = BeautifulSoup(requests.get(url).content, "html.parser")

  data = soup.find('div', {'id': 'data'}).findAll('td')

  all_products = []
  product = {}
  counter = 0
  product_details = ''
  availablility = []

  for td in data:
    product_name = td.find('a')
    if not product_name:
      product_details += ' ' + td.text
    else:
      if 'Ebay' not in product_name and counter  != 0:
        product[counter] = product_details
        product['link' + str(counter)] = product_name['href']
        all_products.append(product)
        counter += 1
        product_details = product_name.text
      else:
        counter += 1
        product_details = product_name.text

  # all_products[1][1] = 'Available Bundle: Console w/Extra Controller & COD:Cold War : Walmart CA  Out of Stock $809.96 Nov 12 - 11:12 AM'
  for i in range(len(all_products)):
    product = all_products[i][i+1]
    if 'Available' in product:
      availablility.append({'details': product, 'link' : all_products[i]['link' + str(i + 1)]})

  return availablility
  


  