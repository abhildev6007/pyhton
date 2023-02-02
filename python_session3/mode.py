given_list = [1,2,3,2,4,5,5,5,6,3,6]



def find_mode(given_list):
    count = 0
    mode = given_list[0]
    
    for number in given_list:
        freequency = given_list.count(number)
        if count<freequency:
            count = freequency
            mode = number
    
    print("mode = ", mode) 

find_mode(given_list)