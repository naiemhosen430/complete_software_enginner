# Task 5: File Handling


# Write a Python program that:

# 1: Opens a new file in write mode.
# 2: Writes a few lines of text to the file.
# 3: Closes the file.
# 4: Opens the file in read mode and prints its content.

# Solution
file_name = "myFile.py"

myfile = open(file_name, "w")
myfile.write("print(\"hello world\")")
myfile.close()

openFile = open(file_name, "r")
print(openFile.read())


# Completed