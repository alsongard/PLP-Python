"""
public: no underscore
protected: single underscore
private: double undesscore
"""

class BankSystem:
    def __init__(self):
        self.acc_balance = 8000
        self._acc_number = 1234
        self.__acc_pin = 0000
    
bank1 = BankSystem()
print(f'The account balance is : {bank1.acc_balance}')
print(f'The account number is : {bank1._acc_number}')
# print(f'The account pin is : {bank1.__acc_pin}') # result in AttributeError: 'BankSystem' object has no attribute '__accPin'