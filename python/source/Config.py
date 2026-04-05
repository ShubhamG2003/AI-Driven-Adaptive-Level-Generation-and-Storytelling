import pandas as pd
from LDA import BuildModelLDA,GetPredictionLDA
from Bagging import BuildModelBAGHO,BuildModelBAGHT,GetPredictionBAGHO,GetPredictionBAGHT
from Boost import BuildModelBOOSTHO,BuildModelBOOSTHT,GetPredictionBOOSTHO,GetPredictionBOOSTHT
from Stacking import BuildModelSTACKHO,BuildModelSTACKHT,GetPredictionSTACKHO,GetPredictionSTACKHT


modelList = [
   "BAG-0", 
   "BAG-1", 
   "BOOST-0", 
   "BOOST-1", 
   "STACK-0", 
   "STACK-1", 
   "LDA"
   ]
initfn = [
        BuildModelBAGHO,
        BuildModelBAGHT,
        BuildModelBOOSTHO,
        BuildModelBOOSTHT,
        BuildModelSTACKHO,
        BuildModelSTACKHT,
        BuildModelLDA,
    ]
predictfn = [
        GetPredictionBAGHO,
        GetPredictionBAGHT,
        GetPredictionBOOSTHO,
        GetPredictionBOOSTHT,
        GetPredictionSTACKHO,
        GetPredictionSTACKHT,
        GetPredictionLDA,
    ]

class Config:
  def __init__(self, name:str, fname:str="../data/GameAttributes.csv",target_col:str="Skill"):
    self.name = name            # AI model name
    self.fname = fname          # file name to train model
    if name not in modelList:
        name = "LDA"
    idx = modelList.index(name)
    self.init = initfn[idx]
    self.model = self.init(fname)
    self.predict =predictfn[idx]

    self.ColumnName=[]                      #Read column names from .csv file
    df= pd.read_csv(self.fname, nrows=1)
    self.ColumnName=df.columns.to_list()
    self.ColumnName.remove(target_col)      #Remove label column as this will be predicted.
    self.model # type: ignore

