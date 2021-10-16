#Programming Assignment 03
#Written by : Surya Venkatesh Vijjana
# Date : Sep 23,2021

#Functions to calculate Area and Perimeter of geometric shapes

import math
pi=round(math.pi,2)

#Function to calculate area and circumference of circle
def circle(radius):
    area=pi*radius*radius
    perimeter=2*pi*radius

    return [area,perimeter]

#Function to calculate area and perimeter of square
def square(side):
    area=side*side
    perimeter=4*side

    return [area,perimeter]  

#Function to calculate area and perimeter of rectangle
def rectangle(length,width):
    area=length*width
    perimeter=2*(length+width)

    return [area,perimeter]

#Function to calculate area and perimeter of rhombus
def rhombus(d1,d2,side):
    area=0.5*d1*d2
    perimeter=4*side

    return [area,perimeter]    
