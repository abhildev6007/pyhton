def fahrenheit_to_celsius(temperature_in_fahrenheit):
    temperature_in_celsius = []
    for temperature in temperature_in_fahrenheit:
        celsius = (float(temperature) - 32 )/1.8
        temperature_in_celsius.append(celsius)
    return(temperature_in_celsius)

input_temperature = input("Enter the list of temperature in fahrenheit separated by space as int or float :")
temperature_in_fahrenheit = input_temperature.split()
print(temperature_in_fahrenheit)
temperature_in_celsius = fahrenheit_to_celsius(temperature_in_fahrenheit)
print(temperature_in_celsius)