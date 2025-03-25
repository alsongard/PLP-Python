# strings
# strings are immutable


myString="hello_world_welcome_to_pthon_strings"
# characters in a string can be accessed using  indexig and slicig
print(myString[0]) # h
print(myString[0:10]) # hello_worl


print("\n")
# one can also use the enumarate() on a string
for count_value, item in enumerate(myString):
    print(f"index is {count_value} & character: {item}")



# comparing strings 
my_string_a = "Jesus is King"
my_string_b = "Jesus is King"

print(my_string_a == my_string_b)

# get the length of a string use
print(len(my_string_b))


# string membership test
print("a" in my_string_a) # false
print("K" in my_string_a) # True