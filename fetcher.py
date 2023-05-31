import requests
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin

def fetch_data(url):
    # Set request headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    # Send HTTP request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None, None

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Navigate and search HTML parse tree
    book_divs = soup.find_all('div', {'class': 'product_pod'})

    if not book_divs:  # If no product_pod divs were found
        print(f"No 'product_pod' divs were found in {url}")

    data = []
    for book_div in book_divs:
        title = book_div.h3.a['title']
        price = book_div.find('p', class_='price_color').text
        availability = book_div.find('p', class_='instock availability').text.strip()
        rating = book_div.find('p', class_='star-rating')['class'][1]
        data.append([title, price, availability, rating])


    if not data:  # If no items were fetched
        print(f"No items were fetched from {url}")

    # Check if there is a next page
    next_page = soup.find('li', class_='next')
    next_page_url = next_page.a['href'] if next_page else None

    # Delay the next request
    sleep(1)

    return data, next_page_url