# the with is used to close the open() function ensuring efficient use of memory
with open('myText.txt', 'a') as file:
    file.write("\nsearching for another day, while am still winning")


with open('myText.txt', 'r') as file:
    file_data = file.read()

print(file_data)