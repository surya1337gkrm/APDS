#Programming Assignment 02
#Written by : Surya Venkatesh Vijjana
# Date : Sep 13,2021

import random

username=input('Please Enter User Name: ')

#Defining a function to display menu and perform required operations
def displayMenu():
    print('1 - Addition\n2 - Subtraction\n3 - Exit')
    userChoice=int(input('Please Enter Your Choice : '))

    if userChoice==1:
        #generating two numbers in range [0,10] : Numbers will be integers from 0 to 9.
        num1=int(random.random()*10)
        num2=int(random.random()*10)

        orgResult=num1+num2
        userInput=int(input('Enter the sum of the given two numbers\n{0} and {1}\nSum : '.format(num1,num2)))

        if(orgResult==userInput):
            enterKey=input('Well done. Press Enter Key to Continue.')
            #When enter key is pressed, input value will be empty string and its a boolean value.
            #not will help us to change the value to true and enters into the if condition to display the menu again.
            if(not enterKey):
                displayMenu()


        else:
            enterKey=input('Sorry,The correct answer is {0}. Press Enter Key to Continue.'.format(orgResult)) 
            if(not enterKey):
                displayMenu()  


    elif userChoice==2:
        num1=int(random.random()*10)
        num2=int(random.random()*10)

        #if both numbers are same,Terminate the operation and display the menu again to get a new choice from the user.
        if(num1==num2):
            print('Both Numbers are same and the difference is 0')
            displayMenu() #displays the menu again
            exit(0) #exits from executing this condition

        #check if number 2 is greater than number 1. if yes, swap the numbers as difference should always be greater than 0.
        if(num2>num1):
            num1,num2=num2,num1 #swapping the numbers.
            
        orgResult=num1-num2
        userInput=int(input('Enter the difference of the given two numbers\n{0} and {1}\nDifference : '.format(num1,num2)))

        if(orgResult==userInput):
            enterKey=input('Well done. Press Enter Key to Continue.')
            if(not enterKey):
                displayMenu()


        else:
            enterKey=input('Sorry,The correct answer is {0}. Press Enter Key to Continue.'.format(orgResult)) 
            if(not enterKey):
                displayMenu()

    elif userChoice==3:
        print('Thank You,',username)  #exit from the program case   

    else:
        print('Invalid Choice. Please Enter a Valid Choice') #invalid user choice 
        displayMenu()


displayMenu()


