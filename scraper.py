import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:
        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        data.append([title, price, availability])

    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Title",
            "Price",
            "Availability"
        ])

        writer.writerows(data)

    print("Dane zapisane do books.csv")

else:
    print(f"Błąd: {response.status_code}")