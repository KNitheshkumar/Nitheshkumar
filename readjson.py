from json import *
file = open('data.json', 'r')
p = file.read()
x = loads(p)
print(x)