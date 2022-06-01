import requests
from bs4 import BeautifulSoup

with open("books.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "xml")
for book in bs.find_all("book"):
    title = book.find("title").text
    price = book.find("price").text
    print(f"{title:20} {price:5}")


