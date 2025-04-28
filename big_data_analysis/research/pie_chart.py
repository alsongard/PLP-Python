import pandas as plt
import matplotlib.pyplot as plt

fruits = ['apple', 'banana', 'pineapple', 'watermelon']
fruit_size = [50, 10, 60, 30]

# plot
plt.pie(fruit_size, labels=fruits, autopct='%1.1f%%', startangle=90)
plt.title('Fruits distribution')
plt.show()

"""
auto_pct: used to format the percentage labels on each wedge(pie) of the piechart

auto_pct='%1.1f%%'
the first: % : indicates that the end of the value will have a percentage
sign
the 1.1f shows that:
1 : width for the value
.1 : value after the decimal (which is one)
f: datatype which is a float number
"""