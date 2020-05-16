import requests
from bs4 import BeautifulSoup

URL = 'https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/3ec8448d-ebc8-8fc0-e0b7-9e8ef6c79918/rss'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
