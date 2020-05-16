import requests
from bs4 import BeautifulSoup

URL = 'https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
