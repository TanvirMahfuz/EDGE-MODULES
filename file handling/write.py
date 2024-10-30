# Open a file in write mode (creates a new file or overwrites an existing one)
file = open('example.txt', 'w')

# Write a string to the file
file.write("Hello, World!\n")

# Write multiple lines
lines = ["This is line 1.\n", "This is line 2.\n"]
file.writelines(lines)

# Close the file
file.close()
