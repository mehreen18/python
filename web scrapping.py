print("hiiiiii")

import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"
page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")


title = soup.find("h1")
print(title.text)



import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Saari books nikalo
books = soup.find_all("article", class_="product_pod")

print(f"Total books: {len(books)}")
print("─" * 40)

for book in books:
    title  = book.find("h3").find("a")["title"]
    price  = book.find("p", class_="price_color").text.strip()
    rating = book.find("p", class_="star-rating")["class"][1]

    print(f"Title  : {title}")
    print(f"Price  : {price}")
    print(f"Rating : {rating}")
    print("─" * 40)