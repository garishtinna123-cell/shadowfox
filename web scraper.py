import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://example.com"

# Send HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract page title
title = soup.title.text
print("Page Title:", title)

# Extract all links
print("\nLinks on the page:")
for link in soup.find_all("a"):
    print(link.get("href"))