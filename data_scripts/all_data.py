import requests
import csv

# Replace with your API credentials
API_KEY = "Xo*LsNEYD*gXG7WrW3fl"
EMAIL = "brandon_concepcion@berkeley.edu"
BASE_URL = "https://api.acleddata.com/acled/read"

def query_all_data():
    # Parameters for the API request
    params = {
        "key": API_KEY,
        "email": EMAIL,
        "limit": 0  # Request all data; pagination is recommended for large datasets
    }

    try:
        # Make the GET request to the API
        response = requests.get(BASE_URL, params=params)
        
        # Check the response status code
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print(f"Total Records Retrieved: {data.get('count')}")
                return data.get("data")
            else:
                print("API Error:", data.get("messages"))
                return None
        else:
            print("HTTP Error:", response.status_code, response.text)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def write_to_csv(data, filename="acled_data.csv"):
    # Ensure data exists
    if not data:
        print("No data to write to CSV.")
        return

    try:
        # Open the CSV file for writing
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write the header using keys from the first row
            header = data[0].keys()
            writer.writerow(header)
            
            # Write the data rows
            for row in data:
                writer.writerow(row.values())
        
        print(f"Data successfully written to {filename}")
    except Exception as e:
        print("An error occurred while writing to CSV:", e)

# Example usage
if __name__ == "__main__":
    all_data = query_all_data()
    if all_data:
        write_to_csv(all_data)
