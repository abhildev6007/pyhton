def miles_to_km(list_of_miles):
    list_of_km = []
    for value_in_mile in list_of_miles:
        value_in_km = value_in_mile * 1.60934
        list_of_km.append(value_in_km)
        
    return(list_of_km)

list_of_miles = [1,2,3,10]
list_of_km = miles_to_km(list_of_miles)
print(list_of_km)