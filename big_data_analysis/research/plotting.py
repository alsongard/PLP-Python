import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    [
        ['Fully Paid', 1, 1],
        ['Fully Paid', 1, 1],
        ['Fully Paid', 1, 0],
        ['Defaulted', 1, 0],
        ['Defaulted', 1, 0]
    ], columns=['LoanStatus', 'B', 'C']
)

print(df)

s = df['LoanStatus'].value_counts()
print(f'The values counts in colun LoanStatus is :\n{s}')

plt.pie(s, labels=s.index)
plt.show()