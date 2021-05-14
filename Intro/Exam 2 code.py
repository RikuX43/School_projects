import math

#Inputting the perimeter/circumference 
surface_Area = float(input("Enter surface area of shape(s): "))

#Processing the perimeter to area data of shapes
cube = float(math.sqrt(surface_Area / 6)) ** 3

tri_Side = float(math.sqrt(1 / math.sqrt(3) * surface_Area))
tet_Hed = float(math.sqrt((2) / 12) * tri_Side ** 3)

radius = float(math.sqrt(surface_Area / (4 * math.pi)))

sph_Vol = float(4/3 * math.pi * radius ** 3)


#Limiting the floating numbers to 2 decimal places
limit_cube = round(cube, 2)
limit_sphere = round(sph_Vol, 2)
limit_tet = round(tet_Hed, 2)

#Output of the areas with corresponding shapes
print("A cube with that surface area would have a volume of...", limit_cube)
print("A tetrahedron with that surface are would have an volume of...", limit_tet)
print("A circle with that surface area would have an volume of...", limit_sphere)
