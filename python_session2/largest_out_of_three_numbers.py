# Write a function to find and return the largest number out of the given 3 numbers

def largest_number(num1, num2, num3):
    if (num1==num2==num3):
        print("Equal numbers")
    elif (num1>num2):
        if (num1>num3):
            print("Largest number is ", num1)
        else:
            print("Largest number  is ", num3)
    else:
        if (num2>num3):
            print("Largest number is ", num2)
            
        else:
            print("Largest number is ", num3)

num1 = eval(input("Enter a first number :"))
num2 = eval(input("Enter a second number :"))
num3 = eval(input("Enter a third number :"))

largest_number(num1,num2, num3)
            