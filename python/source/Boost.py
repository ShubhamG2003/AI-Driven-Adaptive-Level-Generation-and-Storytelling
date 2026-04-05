from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle


def SaveModelBoostHo(model_BoostHom, fname="../data/model_BoostHom.pk") -> None:
    try:
        fileObj = open(fname, "wb")
    except:
        print(f"file {fname} could not be opened")
        print("Error saving Model...")
    else:
        pickle.dump(obj=model_BoostHom, file=fileObj)
        print("Saved Model...")
        fileObj.close()
    return


# Load the ../data/GameAttributes.csv dataset
# Adjust the path to where your dataset is located
def CreateAndTrainModelBOOSTHO(fname:str = "../data/GameAttributes.csv" ):
    print("Creating and Training Model...")
    dfGame = pd.read_csv(fname)
    # Splitting Attributes and target variable
    dfAttributes = dfGame.drop("Skill", axis=1)
    dfTarget = dfGame["Skill"]
    # Splitting the dataset into training and testing sets
    dfAttribute_train, dfAttribute_test, dfTarget_train, dfTarget_test = (
        train_test_split(dfAttributes, dfTarget, test_size=0.3, random_state=42)
    )
    ModelBoostHo = AdaBoostClassifier(algorithm = "SAMME.R",n_estimators=100, random_state=42)
    ModelBoostHo.fit(dfAttribute_train, dfTarget_train)
    y_pred = ModelBoostHo.predict(dfAttribute_test)
    accuracy = accuracy_score(dfTarget_test, y_pred)
    print(f"Accuracy of BOOSTHO classifier on test set: {accuracy:.2f}")
    return ModelBoostHo


def BuildModelBOOSTHO(fname:str = "../data/GameAttributes.csv",fpname="../data/model_BoostHom.pk"):
    print(f"Loading Model... {fpname}")
    try:
        fileObj = open(fpname, mode="rb")
    except:
        print(f"{fpname}...Model not found")
        print("Creating Model from default DataSet...")
        model_BoostHom = CreateAndTrainModelBOOSTHO(fname)
        SaveModelBoostHo(model_BoostHom)
    else:
        model_BoostHom = pickle.load(fileObj)
        fileObj.close()
    return model_BoostHom


def GetPredictionBOOSTHO(s: str, model_BoostHom , coln:list) -> str:
    score = [int(e) if e.isdigit() else e for e in s.split(",")]
    dfNewPlayer = pd.DataFrame(
        [score],
        columns=coln,
    )
    result = str(model_BoostHom.predict(dfNewPlayer))
    return result

def SaveModelBoostHt(model_BoostHt, fname="../data/model_BoostHt.pk") -> None:
    try:
        fileObj = open(fname, "wb")
    except:
        print(f"file {fname} could not be opened")
        print("Error saving Model...")
    else:
        pickle.dump(obj=model_BoostHt, file=fileObj)
        print("Saved Model...")
        fileObj.close()
    return


# Load the ../data/GameAttributes.csv dataset
# Adjust the path to where your dataset is located
def CreateAndTrainModelBOOSTHT(fname:str= "../data/GameAttributes.csv"):
    print("Creating and Training Model...")
    dfGame = pd.read_csv(fname)
    # Splitting Attributes and target variable
    dfAttributes = dfGame.drop("Skill", axis=1)
    dfTarget = dfGame["Skill"]
    # Splitting the dataset into training and testing sets
    dfAttribute_train, dfAttribute_test, dfTarget_train, dfTarget_test = (
        train_test_split(dfAttributes, dfTarget, test_size=0.3, random_state=42)
    )
    base_learner = DecisionTreeClassifier(max_depth=1)
    ModelBoostHt = AdaBoostClassifier( algorithm = "SAMME.R",estimator=base_learner , n_estimators=100, random_state=42)
    ModelBoostHt.fit(dfAttribute_train, dfTarget_train)
    y_pred = ModelBoostHt.predict(dfAttribute_test)
    accuracy = accuracy_score(dfTarget_test, y_pred)
    print(f"Accuracy of BOOSTHT classifier on test set: {accuracy:.2f}")
    return ModelBoostHt


def BuildModelBOOSTHT(fname:str = "../data/GameAttributes.csv",fpname="../data/model_BoostHt.pk"):
    print(f"Loading Model... {fpname}")
    try:
        fileObj = open(fpname, mode="rb")
    except:
        print(f"{fpname}...Model not found")
        print("Creating Model from default DataSet...")
        model_BoostHt = CreateAndTrainModelBOOSTHT(fname)
        SaveModelBoostHt(model_BoostHt)
    else:
        model_BoostHt = pickle.load(fileObj)
        fileObj.close()
    return model_BoostHt


def GetPredictionBOOSTHT(s: str, model_BoostHt , coln:list) -> str:
    score = [int(e) if e.isdigit() else e for e in s.split(",")]
    dfNewPlayer = pd.DataFrame(
        [score],
        columns=coln,
    )
    result = str(model_BoostHt.predict(dfNewPlayer))
    return result
