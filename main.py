import streamlit as st
import requests
import pandas as pd

def fetch_data():
    # URL of the API
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error("An error occurred while fetching data:", e)
        return None

def main():
    st.title("API Data Display")

    # Fetch data from the API
    data = fetch_data()

    # Display the fetched data as tables
    if data:
        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Display DataFrame as table
        st.write("Fetched Data:")
        st.write(df)

if __name__ == "__main__":
    main()
