#Find the area of rectangle, square, circle and triangle

from math import pi

print("Area calculation")

def rectangle_area():
  '''this function is for finding area of rectangle'''
  length=float(input("Enter the length value : "))
  breadth=float(input("Enter the breadth value : "))
  area = length * breadth
  print('Area of Rectangle: %0.2f\n' %(area))
	
def square_area():
  '''this function is for finding area of square'''
  side=float(input("Enter the side value : "))
  area = side*side
  print('Area of Square: %0.2f\n' %(area))

def circle_area():
  '''this function is for finding area of circle'''
  radius=float(input("Enter the radius value : "))
  area = pi * radius**2
  print('Area of Circle: %0.2f\n' %(area))

def triangle_area():
  '''this function is for finding area of triangle'''
  base=float(input("Enter the base value : "))
  height=float(input("Enter the height value : "))
  area = 1/2 * base * height
  print('Area of Triangle: %0.2f\n' %(area))

while True:
  print("1.Rectangle\n2.Square\n3.Circle\n4.Triangle\n5.Quit\n")
  choice = int(input("Choose your option : "))
  if choice==1:
    rectangle_area()
  elif choice==2:
    square_area()
  elif choice==3:
    circle_area()
  elif choice==4:
    triangle_area()
  else:
    break
