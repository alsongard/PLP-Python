even_numbers = []
for item in range(0,21):
    if item % 2 == 0:
        even_numbers.append(item)
print(even_numbers)

squared_even_numbers = [item **2 for item in even_numbers]
print(squared_even_numbers)


odd_squared_numbers = [number ** 2 for number in range(0,21) if number % 3== 0]
print(odd_squared_numbers)