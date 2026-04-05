from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle


def SaveModelBagHo(model_bagHom, fname="../data/model_bagHom.pk") -> None:
    try:
        fileObj = open(fname, "wb")
    except:
        print(f"file {fname} could not be opened")
        print("Error saving Model...")
    else:
        pickle.dump(obj=model_bagHom, file=fileObj)
        print("Saved Model...")
        fileObj.close()
    return


# Load the ../data/GameAttributes.csv dataset
# Adjust the path to where your dataset is located
def CreateAndTrainModelBAGHO(fname:str="../data/GameAttributes.csv"):
    print("Creating and Training Model...")
    dfGame = pd.read_csv(fname)
    # Splitting Attributes and target variable
    dfAttributes = dfGame.drop("Skill", axis=1)
    dfTarget = dfGame["Skill"]
    # Splitting the dataset into training and testing sets
    dfAttribute_train, dfAttribute_test, dfTarget_train, dfTarget_test = (
        train_test_split(dfAttributes, dfTarget, test_size=0.3, random_state=42)
    )
    ModelBagHo = RandomForestClassifier(n_estimators=100, random_state=42)
    ModelBagHo.fit(dfAttribute_train, dfTarget_train)
    y_pred = ModelBagHo.predict(dfAttribute_test)
    accuracy = accuracy_score(dfTarget_test, y_pred)
    print(f"Accuracy of BAGHO classifier on test set: {accuracy:.2f}")
    return ModelBagHo


def BuildModelBAGHO(fname="../data/GameAttributes.csv",fpname="../data/model_bagHom.pk"):
    print(f"Loading Model... {fpname}")
    try:
        fileObj = open(fpname, mode="rb")
    except:
        print(f"{fpname}...Model not found")
        print("Creating Model from default DataSet...")
        model_bagHom = CreateAndTrainModelBAGHO(fname)
        SaveModelBagHo(model_bagHom)
    else:
        model_bagHom = pickle.load(fileObj)
        fileObj.close()
    return model_bagHom


def GetPredictionBAGHO(s: str, model_bagHom,coln:list) -> str:
    score = [int(e) if e.isdigit() else e for e in s.split(",")]
    dfNewPlayer = pd.DataFrame(
        [score],
        columns=coln,
    )
    result = str(model_bagHom.predict(dfNewPlayer))
    return result

def SaveModelBagHt(model_bagHt, fname="../data/model_bagHt.pk") -> None:
    try:
        fileObj = open(fname, "wb")
    except:
        print(f"file {fname} could not be opened")
        print("Error saving Model...")
    else:
        pickle.dump(obj=model_bagHt, file=fileObj)
        print("Saved Model...")
        fileObj.close()
    return


# Load the ../data/GameAttributes.csv dataset
# Adjust the path to where your dataset is located
def CreateAndTrainModelBAGHT(fname:str="../data/GameAttributes.csv"):
    print("Creating and Training Model...")
    dfGame = pd.read_csv(fname)
    # Splitting Attributes and target variable
    dfAttributes = dfGame.drop("Skill", axis=1)
    dfTarget = dfGame["Skill"]
    # Splitting the dataset into training and testing sets
    dfAttribute_train, dfAttribute_test, dfTarget_train, dfTarget_test = (
        train_test_split(dfAttributes, dfTarget, test_size=0.3, random_state=42)
    )
    base_learner = DecisionTreeClassifier()
    ModelBagHt = BaggingClassifier(estimator=base_learner , n_estimators=100, random_state=42)
    ModelBagHt.fit(dfAttribute_train, dfTarget_train)
    y_pred = ModelBagHt.predict(dfAttribute_test)
    accuracy = accuracy_score(dfTarget_test, y_pred)
    print(f"Accuracy of BAGHT classifier on test set: {accuracy:.2f}")
    return ModelBagHt


def BuildModelBAGHT(fname ="../data/GameAttributes.csv",fpname="../data/model_bagHt.pk"):
    print(f"Loading Model... {fpname}")
    try:
        fileObj = open(fpname, mode="rb")
    except:
        print(f"{fpname}...Model not found")
        print("Creating Model from default DataSet...")
        model_bagHt = CreateAndTrainModelBAGHT(fname)
        SaveModelBagHt(model_bagHt)
    else:
        model_bagHt = pickle.load(fileObj)
        fileObj.close()
    return model_bagHt


def GetPredictionBAGHT(s: str, model_bagHt,coln:list) -> str:
    score = [int(e) if e.isdigit() else e for e in s.split(",")]
    dfNewPlayer = pd.DataFrame(
        [score],
        columns=coln,
    )
    result = str(model_bagHt.predict(dfNewPlayer))
    return result
