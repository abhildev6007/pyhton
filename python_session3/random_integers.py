import random
def get_list_of_random_integer(lenth_of_list):
    n = 0
    list_of_integer = []

    while n < lenth_of_list:
        list_of_integer.append(random.randint(0,100))
        n += 1
        
    return list_of_integer

lenth_of_list = int(input("Please enter length of list as integer : "))
print(get_list_of_random_integer(lenth_of_list))