# Web Scraping and Data Encryption

## Objective
This project demonstrates how to:
- Scrape structured data from a public website using Python.
- Apply basic data security using encryption.
- Handle web data ethically and responsibly.

## Tools Used
- Python 3.14
- Libraries: requests, beautifulsoup4, pandas, cryptography
- IDE: Visual Studio Code

## Website Scraped
Books to Scrape  
http://books.toscrape.com  
A practice site for web scraping with book listings and metadata.

## Files
- `scrape.py`: Scrapes book data and saves it to CSV.
- `books_data.csv`: Raw scraped data.
- `encrypt.py`: Encrypts the CSV file using Fernet encryption.
- `books_data_encrypted.csv`: Encrypted version of the data.
- `encryption.key`: Secret key used for encryption and decryption.
- `README.md`: Project documentation.

## Data Fields Extracted
- Title
- Price
- Rating
- Availability

## Security Feature
Used Fernet encryption from the cryptography library to encrypt the CSV file. The key is stored in a separate file (`encryption.key`).

## Ethical Practices
- Scraped only a few pages to avoid overloading the server.
- Used a user-agent header to mimic browser behavior.
- Added a delay between requests.
- Verified that the site allows scraping.
