import requests
import re

def get_pages(link):
  pages_to_visit = []
  pages_to_visit.append(link)
  pattern = re.compile('https?')
  while pages_to_visit:
    current_page = pages_to_visit.pop(0)
    page = requests.get(current_page)
    for url in re.findall('<a href="([^"]+)">', str(page.content)):
      if url[0] == '/':
        url = current_page + url[1:]
      if pattern.match(url):
        pages_to_visit.append(url)
    yield current_page

webpage = get_pages('http://www.example.com')
for result in webpage:
  print(result)