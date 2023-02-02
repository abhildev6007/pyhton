import random
def get_list_of_random_integer(lenth_of_list, min, max):
    n = 0
    list_of_integer = []

    while n < lenth_of_list:
        list_of_integer.append(random.randint(min,max))
        n += 1
        
    return list_of_integer

lenth_of_list = int(input("Please enter length of list as integer : "))
min = int(input("Please enter min value of list as integer : "))
max = int(input("Please enter max value of list as integer : "))

print(get_list_of_random_integer(lenth_of_list,min,max))