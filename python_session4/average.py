def find_average(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num
        average = sum / 4
    return average

num_list = []
for i in range(4):
    value = eval(input("Enter the number to the list : "))
    num_list.append(value)

average = find_average(num_list)
print("Average =", average)