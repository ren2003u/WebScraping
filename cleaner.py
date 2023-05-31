import pandas as pd

def clean_data(data):
    # Convert list of lists to a pandas DataFrame
    df = pd.DataFrame(data, columns=['Title', 'Price', 'Availability', 'Rating'])
    return df