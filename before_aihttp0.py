file = open('example.txt')
try:
    lines = file.readlines()
finally:
    file.close()
