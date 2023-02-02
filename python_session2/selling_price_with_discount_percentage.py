# Write a function to find the selling price of the book when the list price is given. For the purpose of this problem assume that the discount is 10
# Extend the above function to take 2  more arguments  discount_percentage and binding_type. If binding_type is "HB" no discount is applicable even if the discount percentage is provided as an argument. There is no default discount %age.

def selling_price_calcultion(list_price, discount_percentage, binding_type):
    if (binding_type == 'HB'):
        selling_price = list_price
    else:
        selling_price = list_price - (list_price * discount_percentage / 100)
        
    print("Selling price = ", selling_price)

list_price = eval(input("Enter the list price of the book as int or float : "))
discount_percentage = eval(input("Enter the list discount percentage of the book as int or float : "))
binding_type = input("Enter the binding type of the book (eg:HB) : ")

selling_price_calcultion(list_price, discount_percentage, binding_type.upper())