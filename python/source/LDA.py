"""
Apply LDA Algorithm on GameAttribute Dataset and classify skill grade 
Save and restore trained mode.
"""

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
import pickle

#from Config import *
#from Ensemble import getColumnName


def SaveModelLDA(model_lda, fname="../data/model_lda.pk") -> None:
    try:
        fileObj = open(fname, "wb")
    except:
        print(f"file {fname} could not be opened")
        print("Error saving Model...")
    else:
        pickle.dump(obj=model_lda, file=fileObj)
        print("Saved Model...")
        fileObj.close()
    return


# Load the GameAttributes.csv dataset
# Adjust the path to where your dataset is located
def CreateAndTrainModelLDA(fname="../data/GameAttributes.csv"):
    print("Creating and Training Model...")
    dfGame = pd.read_csv(fname)
    # Splitting Attributes and target variable
    dfAttributes = dfGame.drop("Skill", axis=1)
    dfTarget = dfGame["Skill"]
    # Splitting the dataset into training and testing sets
    dfAttribute_train, dfAttribute_test, dfTarget_train, dfTarget_test = (
        train_test_split(dfAttributes, dfTarget, test_size=0.2, random_state=42)
    )
    LDAModel = LinearDiscriminantAnalysis()
    LDAModel.fit(dfAttribute_train, dfTarget_train)
    y_pred = LDAModel.predict(dfAttribute_test)
    accuracy = accuracy_score(dfTarget_test, y_pred)
    print(f"Accuracy of LDA classifier on test set: {accuracy:.2f}")
    return LDAModel

def BuildModelLDA(fname ="../data/GameAttributes.csv",fpname="../data/model_lda.pk"):
    print("BuildModelLDA")
    #SaveColumnName()
    print(f"Loading Model... {fpname}")
    try:
        fileObj = open(fpname, mode="rb")
    except:
        print(f"{fpname}...Model not found")
        print("Creating Model from default DataSet...")
        model_lda = CreateAndTrainModelLDA(fname)
        SaveModelLDA(model_lda)
    else:
        model_lda = pickle.load(fileObj)
        fileObj.close()
    return model_lda


def GetPredictionLDA(s: str, model_lda,coln:list) -> str:
    print("GetPredictionLDA (s) :", s)
    score = [int(e) if e.isdigit() else e for e in s.split(",")]
    dfNewPlayer = pd.DataFrame(
        [score],
        #columns=["EnemyKilled", "Treasure", "Time", "PowerUps", "HasKey"],
        columns=coln
    )
    result = str(model_lda.predict(dfNewPlayer))
    return result
