from time import sleep

from bs4 import BeautifulSoup
import requests
import lxml
#
# url = 'https://rabota.by/vacancies/mikrobiolog'
# req = requests.get(url,
#                    headers={
#                        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
#                        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
#                    })
#
# soup = BeautifulSoup(req.text, 'lxml')
# search = soup.find_all('a',class_='serp-item__title')
# for elem in search:
#     microb = elem['href']
#     name = elem.text
#     print(name + ':' + microb)


url = 'https://rabota.by/search/vacancy?text=Python+junior&from=suggest_post&salary=&area=1002&ored_clusters=true&enable_snippets=true'
req = requests.get(url,
                   headers={
                       'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                       'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
                   })
lst_pydev = []
soup = BeautifulSoup(req.text, 'lxml')
search = soup.find_all('a', class_='serp-item__title')
for elem in search:
    pydev = elem['href']
    name = elem.text
    lst_pydev.append(f'{name}:{pydev}')

print(lst_pydev)