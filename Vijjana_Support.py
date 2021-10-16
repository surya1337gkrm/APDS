#Programming Assignment 04 : Support File
#Written by : Surya Venkatesh Vijjana
# Date : Oct 15,2021

#Functions to return Positive/Negative responses.

import random

posRes=['Excellent', 'Very Good', 'Well Done', 'Awesome', 'Good Job', 'Correct']
negRes=['Try Again', 'OOPS', 'Not Quite', 'Look at it Again', 'Sorry']

#function to return random positive response
def posResp():
    return posRes[random.randint(0,len(posRes)-1)]

#function to return random negative response
def negResp():
    return negRes[random.randint(0,len(negRes)-1)]    