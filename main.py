# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

url = "https://en.wikipedia.org/wiki/List_of_tallest_buildings"

# Send HTTP request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Success")
else:
    print("Failure")
