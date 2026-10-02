import math

radius = float(input("enter the radius of the circle:"))
area = math.pi * pow(radius, 2)
print(f"the area of the circle is {round(area,2)}")

perimeter = float(input("enter the radius of the circle:"))
perimeter = 2*math.pi*radius
print(f"the perimeter of the circle is {round(perimeter,2)}")

volume = float(input("enter the radius of the circle:"))
volume = 4/3*math.pi*pow(radius,3)
print(f"the volume of the circle is {round(volume,2)}")
