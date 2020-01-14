import os

if os.path.exists("textfile2.txt"):
    os.remove("textfile2.txt")
else:
    print("The file doesn't exist.")