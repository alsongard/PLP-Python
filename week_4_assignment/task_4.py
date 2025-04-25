"""
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""
file_name = input("Enter name of file: ")
text_data = input("Describe your favorite song and the artist: ")
try:
    with open(file_name, 'r') as file:
        file_data = file.read()
    print(file_data)

    with open(file_name, 'a') as file:
        file.write(text_data)
except FileNotFoundError:
    print(f'file {file_name} does not exist!')
    print('try another filename or check gain')
finally:
    file.close()