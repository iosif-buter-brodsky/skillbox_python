import requests
from bs4 import BeautifulSoup

url = "http://www.columbia.edu/~fdc/sample.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    h3_headers = [h3.text for h3 in soup.find_all('h3')]
    if h3_headers:
        print("Подзаголовки сайта:")
        for header in h3_headers:
            print(header)