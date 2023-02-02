# Write a function to find out the simple interest when principal, number of years and annual rate of interest is given

def simple_Interest_Calculation(principal, no_of_years, rate_of_interest):
    simple_interst = principal*no_of_years*rate_of_interest/100
    return simple_interst

principal = eval(input("Enter the principal amount :"))
no_of_years = eval(input("Enter the number of years :"))
rate_of_interest = eval(input("Enter the rate of interest :"))

simple_interest = simple_Interest_Calculation(principal, no_of_years, rate_of_interest)
print("Simple interest = ", simple_interest)