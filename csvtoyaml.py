import csv
import yaml

csv_file = "iit.csv"
yaml_file = "output.yaml"

data = []
with open(csv_file, mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)
        
output_data = []
for row in data:
    item = {
        "model": "api.college",
        "pk": int(row["pk"]),
        "fields": {
            "name": row["name"],
            "city": row["city"]
        }
    }
    output_data.append(item)
with open(yaml_file, mode="w") as file:
    yaml.dump(output_data, file)

print(f"CSV data has been converted to YAML and saved to {yaml_file}.")