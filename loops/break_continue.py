"""
break: the break statement is used to exit the loop

continue: is used to skip the iteration

"""

guessNumber = int(input("Enter any number that comes to your mind : "))
for number in range(0, guessNumber):
    if number % 2== 0:
        continue
    elif number % 3 == 0:
        print(f"{number} is a multiple of 3")
    elif number % 5== 0:
        print(f"{number} is a multiple of 5 and exiting loop")
        break