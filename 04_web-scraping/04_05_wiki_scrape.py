# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

import requests
from bs4 import BeautifulSoup
import re
import random

def extract_links(page):
  soup = BeautifulSoup(page.text, "html.parser")
  links = [link["href"] for link in soup.find_all("a", {"id": re.compile(r"^mw[a-zA-Z]{2}$")})]

  parsed = []
  for link in links:
    match = re.search(r"^https://en.wikipedia.org/wiki/", link)
    if match:
      parsed.append(link) 

  return parsed

URL = "https://en.wikipedia.org/wiki/Web_scraping"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}

# fetch data from wikipedia page
page = requests.get(URL, headers=headers)

# extract all links and exclude navigation links
links = extract_links(page)

# choose random link
link = random.choice(links)
# fetch data from that wikipedia page
random_page = requests.get(link, headers=headers)
print(page.text)
