from sklearn.model_selection import train_test_split
from sklearn.ensemble import (
    RandomForestClassifier,
    StackingClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

def SaveModelStackHo(model_StackHo, fname="../data/model_StackHo.pk") -> None:
    try:
        fileObj = open(fname, "wb")
    except:
        print(f"file {fname} could not be opened")
        print("Error saving Model...")
    else:
        pickle.dump(obj=model_StackHo, file=fileObj)
        print("Saved Model...")
        fileObj.close()
    return


# Load the ../data/GameAttributes.csv dataset
# Adjust the path to where your dataset is located
def CreateAndTrainModelSTACKHO(fname:str = "../data/GameAttributes.csv"):
    print("Creating and Training Model...")
    dfGame = pd.read_csv(fname)
    # Splitting Attributes and target variable
    dfAttributes = dfGame.drop("Skill", axis=1)
    dfTarget = dfGame["Skill"]
    # Splitting the dataset into training and testing sets
    dfAttribute_train, dfAttribute_test, dfTarget_train, dfTarget_test = (
        train_test_split(dfAttributes, dfTarget, test_size=0.3, random_state=42)
    )
    base_learners = [
        ('dt1', DecisionTreeClassifier(max_depth=3)),
        ('dt2', DecisionTreeClassifier(max_depth=5)),
        ('dt3', DecisionTreeClassifier(max_depth=7)),
    ]
    meta_model = LogisticRegression()
    ModelBoostHo = StackingClassifier(
        estimators=base_learners, final_estimator=meta_model
    )
    ModelBoostHo.fit(dfAttribute_train, dfTarget_train)
    y_pred = ModelBoostHo.predict(dfAttribute_test)
    accuracy = accuracy_score(dfTarget_test, y_pred)
    print(f"Accuracy of STACKHO classifier on test set: {accuracy:.2f}")
    return ModelBoostHo


def BuildModelSTACKHO(fname:str = "../data/GameAttributes.csv",fpname="../data/model_StackHo.pk"):
    print(f"Loading Model... {fpname}")
    try:
        fileObj = open(fpname, mode="rb")
    except:
        print(f"{fpname}...Model not found")
        print("Creating Model from default DataSet...")
        model_StackHo = CreateAndTrainModelSTACKHO(fname)
        SaveModelStackHo(model_StackHo)
    else:
        model_StackHo = pickle.load(fileObj)
        fileObj.close()
    return model_StackHo


def GetPredictionSTACKHO(s: str, model_StackHo , coln:list) -> str:
    score = [int(e) if e.isdigit() else e for e in s.split(",")]
    dfNewPlayer = pd.DataFrame(
        [score],
        columns=coln,
    )
    result = str(model_StackHo.predict(dfNewPlayer))
    return result

def SaveModelStackHt(model_StackHt, fname="../data/model_StackHt.pk") -> None:
    try:
        fileObj = open(fname, "wb")
    except:
        print(f"file {fname} could not be opened")
        print("Error saving Model...")
    else:
        pickle.dump(obj=model_StackHt, file=fileObj)
        print("Saved Model...")
        fileObj.close()
    return


# Load the ../data/GameAttributes.csv dataset
# Adjust the path to where your dataset is located
def CreateAndTrainModelSTACKHT(fname:str = "../data/GameAttributes.csv"):
    print("Creating and Training Model...")
    dfGame = pd.read_csv(fname)
    # Splitting Attributes and target variable
    dfAttributes = dfGame.drop("Skill", axis=1)
    dfTarget = dfGame["Skill"]
    # Splitting the dataset into training and testing sets
    dfAttribute_train, dfAttribute_test, dfTarget_train, dfTarget_test = (
        train_test_split(dfAttributes, dfTarget, test_size=0.3, random_state=42)
    )
    base_learners = [
        ("rf", RandomForestClassifier(n_estimators=100, random_state=42)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("svc", SVC(probability=True, random_state=42)),
    ]
    meta_model = LogisticRegression()
    ModelBoostHo = StackingClassifier(
        estimators=base_learners, final_estimator=meta_model
    )
    ModelBoostHo.fit(dfAttribute_train, dfTarget_train)
    y_pred = ModelBoostHo.predict(dfAttribute_test)
    accuracy = accuracy_score(dfTarget_test, y_pred)
    print(f"Accuracy of STACKHT classifier on test set: {accuracy:.2f}")
    return ModelBoostHo


def BuildModelSTACKHT(fname:str = "../data/GameAttributes.csv",fpname="../data/model_StackHt.pk"):
    print(f"Loading Model... {fpname}")
    try:
        fileObj = open(fpname, mode="rb")
    except:
        print(f"{fpname}...Model not found")
        print("Creating Model from default DataSet...")
        model_StackHt = CreateAndTrainModelSTACKHT(fname)
        SaveModelStackHt(model_StackHt)
    else:
        model_StackHt = pickle.load(fileObj)
        fileObj.close()
    return model_StackHt


def GetPredictionSTACKHT(s: str, model_StackHt , coln:list) -> str:
    score = [int(e) if e.isdigit() else e for e in s.split(",")]
    dfNewPlayer = pd.DataFrame(
        [score],
        columns=coln,
    )
    result = str(model_StackHt.predict(dfNewPlayer))
    return result
