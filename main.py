from library_module import book
books = {
    "Python 101": "Philip Robbins",
    "Data Science": "Jannah Mohd"
}

#Add a new book from user input
title = input("Enter book title: ")
author = input("Enter book author: ")
books[title] = author

#Save to File
with open ("books.txt", "f") as file:
    for t, a in books.items():
        f.write(f"{t}: {a}\n")

#read back from file
with open ("books.txt", "r") as file:
    lines = file.readlines()

print ("\nBook List from file: ")
for line in lines:
    t, a = line.strip().split(":")
    b = book(t, a)
    b.display_info()