#This file genrates sample labeled data for testing purpose.
#file name -'GamesAttributes.csv' labeled variable-'Skill'
from random import randint


"""
Actions/Variables/inputs/ N-inputs
linear classifiction
agression, exploration , avoidance
"""

"""
This program will generate .csv file
containing user activity parametes 
(like aggression,avoidance,exploration...)
which will be used to predict game customization
values (difficulty level,...)using different AI techniques
(ensemble learning : using bagging and boosting)
input  : attribute1,...n,target
output :.csv file
"""

def getBehaviour(n: list, pat: list, maxv: list):
    sumAG = 0.0
    sumEX = 0.0
    sumAV = 0.0
    cntAg = cntEx = cntAv = 0
    for i in range(len(n)):
        if pat[i] == "A":
            sumAG += n[i] / maxv[i]
            cntAg += 1
        elif pat[i] == "E":
            sumEX += n[i] / maxv[i]
            cntEx += 1
        elif pat[i] == "V":
            sumAV += n[i] / maxv[i]
            cntAv += 1
    if cntAg > 0:
        sumAG = sumAG / cntAg
    if cntEx > 0:
        sumEX = sumEX / cntEx
    if cntAv > 0:
        sumAV = sumAV / cntAv
    # print("\nsums [A V E] :",round(sumAG,2),round(sumAV,2),round(sumEX,2))
    if sumAG >= sumAV and sumAG >= sumEX:
        return "A"
    elif sumAV >= sumAG and sumAV >= sumEX:
        return "V"
    else:
        return "E"


def genData(FilePath="../../data/GameAttributes.csv", records=5000):
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pat = ["A", "V", "E", "A", "V", "E", "A", "V", "E"]
    colname = ["A1", "V1", "E1", "A2", "V2", "E2", "A3", "V3", "E3"]
    maxv = [10, 20, 30, 30, 20, 10, 20, 20, 20]
    # maxv=[10,10,10, 10,10,10, 10,10,10]
    # Write header i e column names : Note last colnmae is 'Skill'
    fData = open(FilePath, mode="wt")
    colnames = ""
    for i in range(len(maxv)):
        colnames += colname[i] + "_" + str(maxv[i]) + ","
    colnames += "Skill\n"
    fData.write(colnames)
    for j in range(records):
        for i in range(len(n)):
            n[i] = randint(0, maxv[i])
        b = getBehaviour(n, pat, maxv)
        ln = ""
        for x in n:
            ln += str(x) + ","
        ln += b
        ln += "\n"
        fData.write(ln)
    fData.close()
#--------------------------------------------------------------------

def getTarget(n: list, pat: list, maxv: list):
    m = max(n)
    idx = n.index(m)
    #print(m,idx,pat[idx])
    return pat[idx]


def genDataPCK(FilePath="../../data/GAPCK.csv", records=500):
    n = [1, 2, 3]
    pat = ["P", "C", "K"]
    colname = ["Powerups", "Coins", "Keys"]
    maxv = [6, 6, 6]
    # Write header i e column names : Note last colnmae is 'Skill'
    fData = open(FilePath, mode="wt")
    colnames = ""
    for i in range(len(maxv)):
        colnames += colname[i] + "_" + str(maxv[i]) + ","
    colnames += "Skill\n"
    fData.write(colnames)
    for j in range(records):
        for i in range(len(n)):
            n[i] = randint(0, maxv[i])
        b = getTarget(n, pat, maxv)
        ln = ""
        for x in n:
            ln += str(x) + ","
        ln += b
        ln += "\n"
        fData.write(ln)
        print(ln,end='')
    fData.close()

genDataPCK()
