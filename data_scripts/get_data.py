import requests
import csv

# Replace with your ACLED email and access key
email = 'brandon_concepcion@berkeley.edu'
access_key = 'Xo*LsNEYD*gXG7WrW3fl'

# Define the API endpoint
url = 'https://api.acleddata.com/acled/read'

# Set up parameters
max_records = 10000  # Total number of records to fetch
batch_size = 500  # Fetch records in batches (adjust based on API limits)
current_offset = 0  # Start offset
all_data = []  # List to store all fetched data

while len(all_data) < max_records:
    # Request the data in batches
    params = {
        'email': email,
        'key': access_key,
        'limit': batch_size,
        'offset': current_offset,
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        batch_data = response.json().get("data", [])
        if not batch_data:  # Stop if no more data is returned
            break
        
        all_data.extend(batch_data)
        current_offset += batch_size  # Update offset for the next batch
        
        print(f"Fetched {len(batch_data)} records. Total so far: {len(all_data)}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        break

# Save the data to a CSV file
if all_data:
    csv_file = "acled_data_10000.csv"
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(all_data[0].keys())
        
        # Write the data rows
        for record in all_data:
            writer.writerow(record.values())
    
    print(f"Data successfully saved to {csv_file}")
else:
    print("No data fetched.")
