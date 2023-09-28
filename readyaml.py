from yaml import *
with open("yaml_file.yaml","r") as f:
    c= safe_load(f)
print(c)