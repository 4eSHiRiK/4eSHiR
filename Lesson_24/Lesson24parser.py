from bs4 import BeautifulSoup
import requests

response = requests.get('https://av.by/').text
# print(response)

soup = BeautifulSoup(response, 'lxml')
data = soup.find_all('li', class_='catalog__item')[:2]
# print(data)
for item in data:
    url = item.find('a', class_="catalog__link")
    name = item.find('span', class_="catalog__title").text
    print(url,name)
#     res = requests.get(url).text
#     autos = BeautifulSoup(response, 'lxml')
#     autos_items = soup.find_all('div', class_='listing-item listing-item--top')
#     for i in autos_items:
#         auto_name = i.find('span', class_='link-text').text
#         price = i.find('div', class_='listing-item__price').text
#         print(auto_name,price)

# response =requests.post('https://evroopt.by/?wc-ajax=get_refreshed_fragments',headers={
#     'User-Agent':''
# })






# response = requests.get('https://evroopt.by/')