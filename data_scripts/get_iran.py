import requests
import csv

# ACLED API credentials
user_email = 'brandon_concepcion@berkeley.edu'
api_key = 'Xo*LsNEYD*gXG7WrW3fl'

# Define the API endpoint
api_url = 'https://api.acleddata.com/acled/read'

# Set up parameters for filtering the last 500 conflicts in Iran
params = {
    'email': user_email,
    'key': api_key,
    'country': 'Iran',  # Filter for events in Iran
    'limit': 500,  # Limit the results to the last 500
    'format': 'json'
}

# Make the API request
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json().get("data", [])
    
    # Save the data to a CSV file
    if data:
        csv_file_name = "datasets/iran_last_500_conflicts.csv"
        with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(data[0].keys())
            
            # Write the data rows
            for record in data:
                writer.writerow(record.values())
        
        print(f"Last 500 conflicts successfully saved to {csv_file_name}")
    else:
        print("No data found.")
else:
    print(f"Error: {response.status_code} - {response.text}")