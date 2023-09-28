import json
import csv

csv_file = open("csv.csv", 'r')
csv_reader = csv.reader(csv_file)
field_names = next(csv_reader)
data = []

for row in csv_reader:
    data.append(dict(zip(field_names, row)))

json_dump = json.dumps(data)
json_file = open("data.json", "w")
json_file.write(json_dump)
csv_file.close()
json_file.close()