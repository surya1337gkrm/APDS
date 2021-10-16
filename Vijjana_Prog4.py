#Programming Assignment 04 : Main File
#Written by : Surya Venkatesh Vijjana
# Date : Oct 15,2021

#import positive and negative response functions from Support file
from Vijjana_Support import *
import random

#Multi-Dimensional List which has details about each operation
#First item : Operation
#Second item : Number of Attempts
#Third Item : Successful Attempts
#Fourth Attempt : Failed Attempts
tracker=[['Addition',0,0,0],['Subtraction',0,0,0],['Multiplication',0,0,0],['Division',0,0,0]]

username=input('Please Enter User Name: ')

#generating two numbers in range [0,10**n] : Numbers will be integers from 0 to 9/99/999 for n=1/2/3.
#generate number with user defined digits

def genTwoNumbers(n):
    num1=int(random.random()*10**n)
    num2=int(random.random()*10**n)

    return num1,num2

#Defining a function to display menu and perform required operations
def displayMenu():
    print('\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Exit')
    userChoice=int(input('\nPlease Enter Your Choice : '))
    if(userChoice==5):
        
        #Print total attempts,total successful attempts and total failed attempts per each operation type
        for i in range(0,len(tracker)):
            print('\nOperation Type : {0}\nTotal Number of Attempts : {1}\nTotal Number of Successful Attempts : {2}\nTotal Number of Failed Attempts : {3}\n'.format(tracker[i][0],tracker[i][1],tracker[i][2],tracker[i][3]))
        print('\nThank You,',username) #exit case
    else:    
        digits=int(input('\nChoose single digit, double, or triple digits numbers for the operations. \nEnter 1 or 2 or 3 : '))
        operationCount=int(input('\nEnter how many times you want to repeat the operation ( Should be >0 ) : '))

        #runs the loop number of times user want to repeat
        while(operationCount>0):

            if userChoice==1:
                
                num1,num2=genTwoNumbers(digits)

                orgResult=num1+num2
                userInput=int(input('\nEnter the sum of the given two numbers\n{0} and {1}\nSum : '.format(num1,num2)))
                
                #update number of trials
                tracker[0][1]=tracker[0][1]+1

                if(orgResult==userInput):
                    #update number of succesful attempts
                    tracker[0][2]=tracker[0][2]+1
                    #prints positive response 
                    print(posResp())

                else:
                    #update number of failed attempts
                    tracker[0][3]=tracker[0][3]+1
                    #prints negative response
                    print(negResp())
                    #if response is wrong, user will be asked to try one more time for the same question
                    print('\nTry One more time.')
                    userInput=int(input('\nEnter the sum of the given two numbers\n{0} and {1}\nSum : '.format(num1,num2)))
                    tracker[0][1]=tracker[0][1]+1
                    if(orgResult==userInput):
                        tracker[0][2]=tracker[0][2]+1
                        print(posResp())

                    else:
                        tracker[0][3]=tracker[0][3]+1
                        # if still fails to answer correctly,returns a negative response and also the correct answer.
                        print(negResp() + ' and correct answer is {0}'.format(orgResult))

            elif userChoice==2:
                
                num1,num2=genTwoNumbers(digits)

                #if both numbers are same,Generate new Numbers.
                while(num1==num2):
                    print('\nBoth Numbers are same and the difference is 0\nGenerating Two New Numbers.')
                    num1=int(random.random()*10**digits)
                    num2=int(random.random()*10**digits)

                #check if number 2 is greater than number 1. if yes, swap the numbers as difference should always be greater than 0.
                if(num2>num1):
                    num1,num2=num2,num1 #swapping the numbers.
                    
                orgResult=num1-num2
                userInput=int(input('\nEnter the difference of the given two numbers\n{0} and {1}\nDifference : '.format(num1,num2)))

                tracker[1][1]=tracker[1][1]+1

                if(orgResult==userInput):
                    tracker[1][2]=tracker[1][2]+1
                    print(posResp())

                else:
                    tracker[1][3]=tracker[1][3]+1
                    print(negResp())
                    print('\nTry One more time.')
                    userInput=int(input('\nEnter the difference of the given two numbers\n{0} and {1}\nDifference : '.format(num1,num2)))
                    
                    tracker[1][1]=tracker[1][1]+1

                    if(orgResult==userInput):
                        tracker[1][2]=tracker[1][2]+1
                        print(posResp())

                    else:
                        tracker[1][3]=tracker[1][3]+1
                        print(negResp() + ' and correct answer is {0}'.format(orgResult))

            elif userChoice==3:
                num1,num2=genTwoNumbers(digits)
                    
                orgResult=num1*num2
                userInput=int(input('\nEnter the Product of the given two numbers\n{0} and {1}\nProduct : '.format(num1,num2)))

                tracker[2][1]=tracker[2][1]+1

                if(orgResult==userInput):
                    tracker[2][2]=tracker[2][2]+1
                    print(posResp())

                else:
                    tracker[2][3]=tracker[2][3]+1
                    print(negResp())
                    print('\nTry One more time.')
                    userInput=int(input('\nEnter the Product of the given two numbers\n{0} and {1}\nProduct : '.format(num1,num2)))

                    tracker[2][1]=tracker[2][1]+1

                    if(orgResult==userInput):
                     tracker[2][2]=tracker[2][2]+1
                     print(posResp())

                    else:
                        tracker[2][3]=tracker[2][3]+1
                        print(negResp() + ' and correct answer is {0}'.format(orgResult))              

            elif userChoice==4:
                num1,num2=genTwoNumbers(digits)
                #Check whether num2 is 0. if Zero generate new numbers
                while(num2==0):
                    print('Number 2 is 0. Generating New numbers.')
                    num1,num2=genTwoNumbers(digits)
                
                    #Integer Division : Quotient will be an integer
                orgResult=num1//num2
                userInput=int(input('\nEnter the Quotient for the given two numbers [ num1//num2 ] \n{0} and {1}\nQuotient : '.format(num1,num2)))

                tracker[3][1]=tracker[3][1]+1
               
                if(orgResult==userInput):
                    tracker[3][2]=tracker[3][2]+1
                    print(posResp())

                else:
                    tracker[3][3]=tracker[3][3]+1
                    print(negResp())
                    print('\nTry One more time.')
                    userInput=int(input('\nEnter the Quotient of the given two numbers\n{0} and {1}\nQuotient : '.format(num1,num2)))

                    tracker[3][1]=tracker[3][1]+1

                    if(orgResult==userInput):
                        tracker[3][2]=tracker[3][2]+1
                        print(posResp())

                    else:
                        tracker[3][3]=tracker[3][3]+1
                        print(negResp() + ' and correct answer is {0}'.format(orgResult)) 

            else:
                print('\nInvalid Choice. Please Enter a Valid Choice') #invalid user choice 
                displayMenu()

            operationCount=operationCount-1 
        displayMenu()       

displayMenu()