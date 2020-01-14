import os

file = open("textfile.txt",'r')
for line in file:
    print(file.readlines())
file.close()