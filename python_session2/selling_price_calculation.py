# Write a function to find the selling price of the book when the list price is given. For the purpose of this problem assume that the discount is 10

def selling_price_calcultion(list_price):
    selling_price = list_price - (list_price/10)
    print("Selling price = ", selling_price)

list_price = eval(input("Enter the list price of the book as int or float : "))
selling_price_calcultion(list_price)