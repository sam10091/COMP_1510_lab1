pi = 3.14159
radius = 0
radius = float(input("enter your radius: "))
double_radius= 2*radius
circumference= 2*pi*radius
print(circumference)
area=pi*radius*radius
print(area)

circumference_double= 2*pi*double_radius
print(circumference_double)
area_double=pi*double_radius*double_radius
print(area_double)
#When we double the radius, circumference would double but the area doesn't double.

area_dif=area_double/area
print("when the radius doubles, area is increased by",area_dif)
circumference_dif=circumference_double/circumference
print("when the radius double, circumference is increased by",circumference_dif)

