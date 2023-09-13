from ShapesLib import Circle, Triangle

#Initializing Circle class adding necessery radius argument, then using get_area()
circle = Circle(100)
print(circle.get_area())
#31415.926535897932

#To make simplier
print(Triangle(10, 10, 10).get_area())
print(Triangle(3, 4, 5).is_right_triangle())
