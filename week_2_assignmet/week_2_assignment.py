my_list=[]
for value in [10, 20, 30, 40]:
    my_list.append(value)

my_list.insert(2, 15)

print(my_list)

my_list.extend([50, 60, 70])

print(my_list)

my_list.pop()
print(my_list)


my_list.sort()
print(my_list)


i = 0
for index,item in enumerate(my_list):
    if item == 30:
        print(f"index is : {index} and item is : {item}")

# 3