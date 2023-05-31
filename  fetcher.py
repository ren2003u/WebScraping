import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    # Send HTTP request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        return None

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Navigate and search HTML parse tree
    table = soup.find('table', {'class': 'wikitable'})
    table_rows = table.find_all('tr')

    data = []
    for row in table_rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    return data