
import requests
from bs4 import BeautifulSoup

URL = "https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="link")

# Look for Server 2016 updates
##server_updates = results.find_all("title", string=lambda t: "title" in t.lower())
##for s_update in server_updates:
##    link = s_update.find("a")["href"]
##    print(s_update.text.strip())
##    print(f"KB here: {link}\n")

# Print out all available updates from the scraped webpage
update_elems = results.find_all("body", class_="body")
for title_elem in title_elems:
    title_elem = title_elem.find("title", class_="title")
    description_elem = job_elem.find("description", class_="description")
    link_elem = job_elem.find("link", class_="link")
    pubDate_elem = pubDate_elem.find("pubDate", class_="pubDate")
    if None in (title_elem, description_elem, link_elem, pubDate_elem):
        continue
    print(title_elem.text.strip())
    print(description_elem.text.strip())
    print(link_elem.text.strip())    
    print(pubDate_elem.text.strip())
    print()