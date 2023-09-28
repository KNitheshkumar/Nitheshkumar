import pandas as pd
import json

# Load JSON data from a file or API response
with open('data.json', 'r') as file:
    json_data = json.load(file)

# Convert JSON to DataFrame
df = pd.json_normalize(json_data)

# Save DataFrame as CSV
df.to_csv('output.csv', index=False)