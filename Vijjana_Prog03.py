#Programming Assignment 03
#Written by : Surya Venkatesh Vijjana
# Date : Sep 23,2021

#program to find area and perimeter/circumference of geometric shapes

#import shapes.py file to access functions defined in the shapes.py file
import shapes

#Function to display the menu and to choose an option from the menu
def displayMenu():
    option=int(input("Choose a Geometric Shape to calculate Area and Perimeter:\n1.Circle\n2.Square\n3.Rectangle\n4.Rhombus\n5.Exit\nSelect an option : "))
    return option

#Function where the calculations will be done based on the user's selected option
def userCalc(option):
    if option==1:
        print("Circle Selected. Formuale to calculate Area and Circumference of the Circle:\n1.Area of the Cirlcle : Pi*radius*radius\n2.Circumference of a circle: 2*Pi*radius")
        radius=int(input("Enter radius of the circle : "))
        result=shapes.circle(radius)
        return result

    elif option==2:
        print("Square Selected. Formuale to calculate Area and Perimeter of the Square:\n1.Area of the Square : side*side\n2.Perimeter of a Square: 4*side")
        side=int(input("Enter side of the square : "))
        result=shapes.square(side)
        return result  

    elif option==3:
        print("Rectangle Selected. Formuale to calculate Area and Perimeter of the Rectangle:\n1.Area of the Rectangle : Length*Width\n2.Perimeter of a Rectangle: 2*(Length+Width)")
        length=int(input("Enter length of the Rectangle : "))
        width=int(input("Enter width of the Rectangle : "))
        result=shapes.rectangle(length,width)
        return result

    elif option==4:
        print("Rhombus Selected. Formuale to calculate Area and Perimeter of the Rhombus:\n1.Area of the Rhombus : 0.5*diagonal1*diagonal2\n2.Perimeter of a Rhombus: 4*side")
        d1=int(input("Enter diagonal1 of the rhombus : "))
        d2=int(input("Enter diagonal2 of the rhombus : "))
        side=int(input("Enter side of the rhombus : "))
        result=shapes.rhombus(d1,d2,side)
        return result   

    #Exits from the execution when option 5. Exit is selected.
    elif option==5:
        print("Thank You.")
        exit()           

    else:
        print("Invalid Option. Choose a New Option.")    
        main()

#Function to display the Area and Circumference/Perimeter based on the shape user selected.
def displayResult(result):
    print("Area : {0}\nPerimeter : {1}".format(result[0],result[1]))
    main()

#Main function where the rest of the functions will be called in an order to display the menu and then calculate the area and perimeter/circumference and to display thr result
def main():
    option=displayMenu()
    result=userCalc(option)
    displayResult(result)
    

main()        