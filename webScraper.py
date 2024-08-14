import requests
from bs4 import BeautifulSoup

url = 'https://runescape.com'  # Replace with the URL you want to scrape

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the page
title = soup.title.text
print(f"Title of the page: {title}")

# Extract all paragraphs
paragraphs = soup.find_all('p')
for i, p in enumerate(paragraphs):
    print(f"Paragraph {i + 1}: {p.text}")
