# Open a file in read mode
filename = 'example.txt'

# Create a file and write content to it
with open(filename, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new file created in Python.\n")