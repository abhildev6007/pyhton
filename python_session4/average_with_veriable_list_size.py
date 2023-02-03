def find_average(num_list):
    sum = 0
    size = len(num_list)
    for num in num_list:
        sum = sum + num
        average = sum / size
    return average

num_list = []
is_enter_value = True

while is_enter_value:
    value = eval(input("Enter the number to the list : "))
    num_list.append(value)
    input_value = input("Do you want to enter new value? Enter 1 if you want to enter new value else enter 0 : ")
    if input_value not in ["0","1"]:
        print("Sorry! Could not understand your input!")
        break
    else:
        is_enter_value = bool(eval(input_value))
        
average = find_average(num_list)
print("Average =", average)