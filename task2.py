employees = [{'Name' : 'Anu', 'age' : 21, 'des': "Junior Developer", "Exp_in_years":1}, {'Name' : 'Pooja', 'age' : 25, 'des': "Senior Developer", "Exp_in_years":4},
            {'Name' : 'Sam', 'age' : 28, 'des': "Senior Developer", "Exp_in_years":8}, {'Name' : 'Priya', 'age' : 27, 'des': "Senior Developer", "Exp_in_years":7},
            {'Name' : 'James', 'age' : 22, 'des': "Junior Developer", "Exp_in_years":2}, {'Name' : 'Ajay', 'age' : 26, 'des': "Senior Developer", "Exp_in_years":5}]

user_input = input("Enter the name of the employee: ")
size = len(employees)
flag = False
for i in range(size):
    dict = employees[i]
    if dict['Name'].upper() == user_input.upper():
        print(dict)
        flag = True
        break
if flag == False:
    print("No user found")  
    