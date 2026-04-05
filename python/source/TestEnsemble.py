"""
This file contains program to test predictions using all ensemble methods.
"""

from Ensemble import BuildModel,GetPrediction

modelList = [
   "BAG-0", 
   "BAG-1", 
   "BOOST-0", 
   "BOOST-1", 
   "STACK-0", 
   "STACK-1", 
   "LDA"
   ]
for i in modelList:
    BuildModel(i)
    str1 = "6,9,13,23,0,5,8,6,10"
    #str1= str(input("Please enter nine integers separated by commas :\n"))
    result = GetPrediction(str1)
    print(str1+" result :",result)
    print("-"*70+"\n")