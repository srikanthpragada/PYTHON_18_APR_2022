import requests
from bs4 import BeautifulSoup

with open("books_attr.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "xml")
for book in bs.find_all("book"):
    title = book["title"]
    price = book["price"]
    print(f"{title:20} {price:5}")


