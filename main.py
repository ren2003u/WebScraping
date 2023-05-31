from urllib.parse import urljoin
from fetcher import fetch_data
from cleaner import clean_data

def main():
    base_url = "http://books.toscrape.com/"
    url = base_url
    all_data = []

    while url:
        raw_data, next_page_url = fetch_data(url)
        if raw_data is None:
            print("Failed to fetch data")
            return
        all_data.extend(raw_data)
        print(f"Fetched {len(raw_data)} items from {url}")  # Print a message after each successful fetch
        # Build the full url for the next page
        url = urljoin(base_url, next_page_url) if next_page_url else None

    print(f"Total items fetched: {len(all_data)}")  # Print total number of items fetched

    df = clean_data(all_data)

    # Save the DataFrame to a CSV file
    df.to_csv('books.csv', index=False)

if __name__ == "__main__":
    main()