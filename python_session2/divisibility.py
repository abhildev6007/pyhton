# Write a function to find if a given number a is divisible by another given number b. - For example, is_divisible(a,b)

def is_divisible(a,b):
    if (a %  b == 0):
        return True
    else:
        return False

num1 = eval(input("Enter a number : "))
num2 = eval(input("Enter another number : "))

divisibility = is_divisible(num1,num2)

if divisibility:
    print(num1, " is divisible by ", num2)
else:
    print(num1, " is not divisible by ", num2)
    