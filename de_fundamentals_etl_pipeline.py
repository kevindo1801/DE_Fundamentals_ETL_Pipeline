"""
Python Extract Load Transform Pipeline Project
"""

# Import packages
import requests
import pandas as pd
from sqlalchemy import create_engine

def extract()-> dict:
    """ Extract data from API """
    API_URL = "https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data"

    try:
        # Make a GET request to the API
        response =  requests.get(API_URL) 
        # Check if response status code indicates success (status 200)
        response.raise_for_status() 
        # Parse the JSON response into Python Dict
        data = response.json()
        # Return parsed data 
        return data

    except requests.exceptions.RequestException as e:
        # This block will run if there was an error during request
        print(f"Error: {e}") # Print error message
        # Returns empty dict if error occured
        return {}

def transform(data):
    """ Transform dataset into desired structure and filters """

    # Create dataframe
    df = pd.DataFrame(data)
    print(f"Row Count:{len(data)}")

    try:
        # Convert YEAR froms string to int
        df["YEAR"] = pd.to_numeric(df["YEAR"], errors="coerce")
        # Filter for specific YEAR
        df = df[(df["YEAR"] == 2013)]
        # Filter for specific State
        df = df[(df["BENE_STATE_DESC"].str.contains("California"))]
        # Reset and drop index
        df = df.reset_index(drop=True)

        if df.empty:
            raise ValueError("The resulting Dataframe is empty after transformation.")
        return df
    # Exception error alert in case Dataframe comes back empty
    except Exception as e:
        return f"Error: {e}"

def load(df):
    """ Load data into a SQLLite database"""

    # Create SQLite engine
    disk_engine = create_engine('sqlite:///my_lite_store.db')
    # Add parameters of table name and engine
    df.to_sql('count_bene', disk_engine, if_exists='replace')

# Main Execution
data = extract()
df = transform(data)
load(df)