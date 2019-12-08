#Cardio Project Trial
#08.12.2019 ~Sedat GUR

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dfile = pd.read_csv("cardio.csv")

##Gelt the list of header
lst = list(dfile.columns)
#print(lst)



#Get the list of products:
tempfile = dfile.groupby([lst[0]]).mean()
plist = tempfile.index.to_list()
pdict = {}
for i in range(len(plist)):
    pdict[i]=plist[i]


#Print the list of products:
print('List of Products')
for key,value in pdict.items():
    print(key,':',value)


prompt_Check = False
while prompt_Check == False:
    #promt user to select to product to be analyzed:
    product_key = int(input('Product To Be Analyzed: '))
    if product_key in pdict:
        prompt_Check = True
    else:
        print('\nGiven Entry is Out of Bounds')


#Get the list of criterieas:
cdict={}
for i in range(len(lst)):
    cdict[i]=lst[i]
    
#print the list of criterias:
print('\nList of analyze criterias')
for key,value in cdict.items():
    if key != 0:
        print(key,':',value) 
#Prompt User For the Criterias:
prompt_Check = False
while prompt_Check == False:
    crit_key = int(input('\nPlease Input Analyze Criteria: '))
    if crit_key in cdict:
        prompt_Check = True
    else:
        print('\nGiven Entry is Out of Bounds')

#Create new datafile with the selected product            
tempdata = dfile[dfile[lst[0]].str.contains(pdict[product_key])]

#plot depending on the given parameters
sns.countplot(x=lst[0], hue=cdict[crit_key], data=tempdata)
plt.show()
 


    











