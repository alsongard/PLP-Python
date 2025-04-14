def calculate_discount(price, discount_percent):
    if (discount_percent >= 20):
        discount = (discount_percent/100) * price
        final_price_discount = price - discount
        print(f"The final price after discount is : {final_price_discount}")
    else:
        return price


price_value = int(input("Enter price value: "))

discount = int(input("Enter discount percentage: "))

original_price_value = calculate_discount(price_value,discount)
if (original_price_value):
    print(f"The original price value is : {original_price_value}")
    