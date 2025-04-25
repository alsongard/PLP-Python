"""
Create a file called input.txt and write at least five lines of text into it.
Write a Python script to:
Read the contents of input.txt.
Count the number of words in the file.
Convert all text to uppercase.
Write the processed text and the word count to a new file called output.txt.
Print a success message once the new file is created.
"""

file_name = input('Enter the name of your file: ')
"""
try:
    with open(file_name, 'r') as file:
        file_data = file.readlines()
        for item in file_data:
            print(item)
        print(file_data)
except FileNotFoundError:
    print(f'Filename {file_name} does not exit!')
"""

words_list = []
try:
    with open(file_name, 'r') as file:
        file_data = file.readlines()
        for sentenceLists in file_data:
            singleSentence = sentenceLists.split()
            for item in singleSentence:
                words_list.append(item)

    print(words_list)
    words_list_length = len(words_list)
    upper_case_word_list = []

    for item in words_list:
        upper_case_word_list.append(item.upper())

    print(upper_case_word_list)

    with open('output.txt', 'w') as file:
        entire_sentence = " ".join(upper_case_word_list) + " " + str(words_list_length)
        file.write(entire_sentence)
except FileNotFoundError:
    print(f'The file : {file_name} does not exist')
finally:
    file.close()
# split() method converts a string to a list, uses the whitespace default
"""
mySentence = "remember me remember me remember me am on my onw remember me am too far gone remember me"
mySentence.split()
['remember', 'me', 'remember', 'me', 'remember', 'me', 'am', 'on', 'my', 'onw', 'remember', 'me', 'am', 'too', 'far', 'gone', 'remember', 'me']
"""