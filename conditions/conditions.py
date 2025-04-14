temp = int(input("Enter temperature value: "))

print(type(temp))

if temp > 30:
    print(f"temperature value is {temp} and it's hot")
elif temp > 20 & temp < 30:
    print(f"Temperature value is {temp} and it's average temperature")
else:
    print(f"Temperature value is {temp} and it's a bit cold.")