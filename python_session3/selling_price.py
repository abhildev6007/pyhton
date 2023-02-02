# Write a function to find the selling price of the book when the list price and discount_percentage are given. Discount percentage should be optional. When no value is provided, the function will assume that the value is 10%



def selling_price_calculate(list_price, discount_percentage=10):
    selling_price = list_price - (list_price*discount_percentage/100)
    print("selling_price = ", selling_price)

list_price = eval(input("Enter the list price in int or float : "))
is_discount = input("Do you want to give the discount percentage (yes/no): ")
if is_discount.upper()=='YES':
    discount_percentage = eval(input("Enter the discount percentage in int or float : "))
    selling_price_calculate(list_price, discount_percentage)
else:
    selling_price_calculate(list_price)