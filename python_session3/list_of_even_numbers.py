import random
def get_list_of_random_integer(lenth_of_list):
    n = 0
    list_of_integer = []

    while n < lenth_of_list:
        number = random.randint(0,100)
        if (number % 2) == 0:
            list_of_integer.append(number)
            n += 1
        
    return list_of_integer

lenth_of_list = int(input("Please enter length of list as integer : "))

print(get_list_of_random_integer(lenth_of_list))