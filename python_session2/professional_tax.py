# Write a function to find out the professional tax applicable for an employee when salary is provided. The professional tax is to be computed at 0.25% of the salary amount. If the salary is less than 10000, professional tax applicable will be zero

def calculate_tax(salary):
    if salary<10000 :
        tax = 0
    else:
        tax = salary * 0.25 / 100

    print("Tax = ", tax)

salary = eval(input("Enter the salary amount : "))
calculate_tax(salary)