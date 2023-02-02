# Write a function to compute and return the arithmetic mean for the values contained in the given list

def arithmentic_mean(numbers):
    no_of_elements_in_list = len(numbers)
    sum = 0
    for number in numbers:
        sum = sum + number
    mean = sum / no_of_elements_in_list
    print("Mean = ", mean)


numbers = [1,2,4,5,6,7,8]
arithmentic_mean(numbers)