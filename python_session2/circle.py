    
# Write a function to compute and return the area of a circle
# Write a function to compute and return the circumference of a circle


def area_of_circle(radius):
    area = 3.14*radius*radius
    return area

def circumference_of_circle(radius):
    circumference = 2*3.14*radius
    return circumference

radius = eval(input("Plz enter the radius of the cirlce to calculate the area and circumference :"))
area = area_of_circle(radius)
circumference = circumference_of_circle(radius)
print("Area of the circle  with radius = ", area)
print("Circumference of the circle  with radius = ", circumference)