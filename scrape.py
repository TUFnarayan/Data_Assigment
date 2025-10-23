import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'User-Agent': 'Mozilla/5.0'}
titles, prices, ratings, availability = [], [], [], []

# Scrape first 3 pages
for page in range(1, 4):
    try:
        url = f'http://books.toscrape.com/catalogue/page-{page}.html'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.select('article.product_pod')

        for book in books:
            title = book.h3.a['title']
            price = book.select_one('.price_color').text.replace('Â£', '£')  # Fix encoding
            rating = book.p['class'][1].capitalize()  # Capitalize rating
            stock = book.select_one('.availability').text.strip()

            titles.append(title)
            prices.append(price)
            ratings.append(rating)
            availability.append(stock)

        time.sleep(1)

    except Exception as e:
        print(f"Error on page {page}: {e}")

# Create and save DataFrame
df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Rating': ratings,
    'Availability': availability
})

df.to_csv('books_data.csv', index=False, encoding='utf-8')
print(" Scraping complete. Data saved in readable format.")
