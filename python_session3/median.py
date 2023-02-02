numbers = [1,2,3,4,5,6,7,8]

def find_median(numbers):
    length_of_list = len(numbers)
   
    if (length_of_list%2 == 0):
        n = int(length_of_list/2)
       
        median = int((numbers[n] + numbers[n+1]) / 2)
    else:
        n = int((length_of_list + 1)/2)
        median = numbers[n]
    
    print("median = ", median)
    
find_median(numbers)