#Automotive Dataset
#30.12.2019 ~Sedat GUR

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dFrame = pd.read_csv('Automobile_data.csv')

#Check if missing value exist in the dataFrame:
print("CHECK FOR NULL VALUES IN THE FRAME:\n")

checker = dFrame.isnull().sum() #return if null object exists
print(checker) #print checker 

boo = 0 #initiate boolean for control loop
lst = list(checker) #get the content of checker into a list

#go thru list to check if True for missing values:
for mem in lst: #control loop
    if mem == True: #if null object exist:
        boo =1 #switch on boolean

if boo == True: #if boolean is switched on:
    print('missing value exist!')
else: #if boolean remains off. 
    print('\nNo missing value in the frame.')

#DFrame Info:
##print("\nPRINT FRAME INFO\n")
##infoFrame = dFrame.info() #get the content type.
##print(infoFrame)

#Search for non-sense data:
print("\nCHECK COLUMNS FOR NON SENSE DATA\n")
NonSenseList = []               #Initiate list for non-sense columns
EvalHeads = dFrame.columns      #Get the column names for evaluation.
numofHeads = len(EvalHeads)-1   #Get the length of colummns names for indexing
memNo = 0                       #initiate indexing for iteration. 

while memNo <= numofHeads:                                  #Iterate thru columns for non-sense members:
    Found = False                                           #Initiate/Reset checkbox if any found
    boo = dFrame[EvalHeads[memNo]].isin(['?','NaN','N/A'])  #Fetch boolean response if given values exist
    boolist = list(boo)                                     #Get the list of boolean response.
    for mem in boolist:                                     #Iterate thru list.
        if mem == True:                                     #If any "True" is seen:
                 Found = True                               #check the Found box. 
    if Found == True:                                       #control if Found box is checked:
        NonSenseList.append(EvalHeads[memNo])               #Add  columns name to the list to notify user.
    memNo = memNo+1                                         #Increment index for next member. 

if len(NonSenseList) != 0:
    print("\nFollowing columns include non-sense contents:")
    Linenumber = 1
    for mem in NonSenseList:
        print(Linenumber,":",mem)
        Linenumber+=1
else:
    print("\nNo columns include non-sense contents.\n")
