class Laptop:
    def __init__(self, laptopBrand, laptopMemorySpace, laptopRAM):
        self.laptop_brand = laptopBrand
        self.laptop_memory = laptopMemorySpace
        self.laptop_ram = laptopRAM
    
    def techProperties(self):
        print(f'The devices specs are: \nlaptopModel: {self.laptop_brand} \nlaptopMemory: {self.laptop_memory} \nlaptopRAM: {self.laptop_ram}')
    
    def goodGaming(self):
        print('Checking if your Laptop is good for gaming: 🤔')
        if (self.laptop_memory >= 800 and self.laptop_ram >= 16):
            print("Your laptop is good for gaming 😊")
        else:
            print('Your laptop is not good for gaming😢')

    def __str__(self):
        return "This Laptop Class with the following attributes: laptop_brand, laptop_memory and laptop_ram"
    

userLaptop1 = Laptop('Samsung', 900, 20)
userLaptop1.techProperties()
userLaptop1.goodGaming()

class Phone(Laptop):
    def __init__(self, phoneBrand, phoneMemSpace, phoneRam):
        self.phone_brand = phoneBrand
        self.phone_memspace = phoneMemSpace
        self.phone_ram = phoneRam
        Laptop.__init__(self, laptopBrand=self.phone_brand, laptopMemorySpace=self.phone_memspace, laptopRAM=self.phone_ram)
    # polymorphism
    def goodGaming(self):
        print('Checking if your phone is good for gaming: 🤔')
        if (self.phone_memspace >= 64 and self.phone_ram >= 8):
            print('Your phone is ood for gaming 😊')
        else:
            print('Your phone is not good for gaming😢')


print('\n\n')
print('using phone class')

userPhone1 = Phone('Samsung', 64,10)
userPhone1.techProperties() # inheritance
userPhone1.goodGaming() # Polymorphism




        