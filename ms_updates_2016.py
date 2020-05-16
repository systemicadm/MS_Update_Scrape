import feedparser
from pandas.io.json import json_normalize
import pandas as pd
import requests
from bs4 import BeautifulSoup

rss_url='https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss'
#Read feed xml data
news_feed = feedparser.parse(rss_url) 

#Flatten data
df_news_feed=json_normalize(news_feed.entries)

#Read articles links
df_news_feed.link.head()




URL = "https://www.monster.com/jobs/search/?q=Software-Developer\
        &where=Australia"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Look for Python jobs
python_jobs = results.find_all("h2", string=lambda t: "python" in t.lower())
for p_job in python_jobs:
    link = p_job.find("a")["href"]
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")

# Print out all available jobs from the scraped webpage
job_elems = results.find_all("section", class_="card-content")
for job_elem in job_elems:
    title_elem = job_elem.find("h2", class_="title")
    company_elem = job_elem.find("div", class_="company")
    location_elem = job_elem.find("div", class_="location")
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()