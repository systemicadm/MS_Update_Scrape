from urllib.request import urlopen
from bs4 import BeautifulSoup

def news(xml_news_url):

    parse_xml_url = urlopen(xml_news_url)
    xml_page = parse_xml_url.read()
    parse_xml_url.close()

    soup_page = BeautifulSoup(xml_page, "xml")
    news_list = soup_page.findAll("item")

    for getfeed in news_list:

        print("\n")
        print('\033[1;33m %s \033[1;m' %getfeed.title.text)
        print('\033[1;32m %s \033[1;m' %getfeed.link.text)
        print('\033[1;35m %s \033[1;m' %getfeed.pubDate.text)
        print("\n")

NEWS_URL = "https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss"

news(NEWS_URL)