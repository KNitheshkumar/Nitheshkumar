import csv
import yaml

csv_file = "West_Bengal29.csv"
yaml_file = "state.yaml"

data = []
with open(csv_file, mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)
        
output_data = []
for row in data:
    item ={
    "model": "api.city",
        "pk": int(row["pk"]),
            "fields":{
            "name": row["name"],
            "state": 29
    
            },
    "y": 8
            
    }
    output_data.append(item)
with open(yaml_file, mode="w") as file:
    yaml.dump(output_data, file,default_flow_style=False, indent=10)
    output_data = '\n---\n'

print(f"CSV data has been converted to YAML and saved to {yaml_file}.")