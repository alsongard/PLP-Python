"""
this file will be used to create a calcutor program
user enters input
perform calculation
"""
import math
number_1 = int(input("Enter any number:" ))
number_2 = int(input("Enter any number:"))

sign = ["+", "-", "*", "/", "%", "**", "squareroot"]
print("Choose either of the symbols shown")
print("\n")
i = 1
for item in sign:
    print(f"{i} : {item}")
    i+=1

symbol = int(input("enter any the corresponding number to the symbol: "))

print(type(number_1))
print(type(number_2))
print(type(symbol))


if symbol == 1:
    operator = "addition"
    result = number_1 + number_2
elif symbol == 2:
    operator ="subtraction"
    result = number_1 - number_2
elif symbol == 3:
    operator = "multiplication"
    result = number_1  * number_2
elif symbol == 4:
    operator = "division"
    result = number_1 / number_2
elif symbol == 5:
    operator = "modulus"
    result = number_1 % number_2
elif symbol == 6:
    operator = "square"
    number_1_square_value = number_1**2
    number_2_square_value = number_2**2
    result = [number_1_square_value, number_2_square_value]
elif symbol == 7:
    operator = "square root"
    number_1_square_root_value = math.sqrt(number_1)
    number_2_square_root_value = math.sqrt(number_2)
    result = [number_1_square_root_value, number_2_square_root_value]

else:
    print("no available operation, choose the correct number")


# if (symbol == 4):
#     symbol -=1
print(f"the {operator} of {number_1} and {number_2} is {result}")