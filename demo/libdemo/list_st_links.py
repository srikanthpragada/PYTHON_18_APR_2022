import requests
from bs4 import BeautifulSoup

#WEBSITE = "http://www.srikanthtechnologies.com"
WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")
for link in bs.find_all("a"):
    href = link['href']
    if not href.startswith("http"):  # relative URL
        href = WEBSITE + "/" + href

    print(href)
