import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the target URL
url = "http://books.toscrape.com/"
headers = {"User-Agent": "Mozilla/5.0"}

# Request the page content with error handling
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check if request was successful
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
    exit()  # Stop the script if there's an error

# If the request is successful, continue with scraping
soup = BeautifulSoup(response.text, "html.parser")

# Find all book titles
books = soup.find_all("h3")

# Collect book titles in a list
titles = [book.get_text() for book in books]

# Save data to a CSV
df = pd.DataFrame({"Title": titles})
df.to_csv("data/books.csv", index=False)
print("Data saved to data/books.csv")
