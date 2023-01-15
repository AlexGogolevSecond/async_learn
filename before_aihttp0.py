file = open('example.txt')
try:
    lines = file.readlines()
finally:
    file.close()

with open('example.txt') as file:
    lines = file.readlines()

a = 0

