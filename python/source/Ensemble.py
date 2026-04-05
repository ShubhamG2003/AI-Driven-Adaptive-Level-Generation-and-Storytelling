"""
Provides different functions to exploite
different AI techniques to prredict trarget variable
for game customization.
input : game.csv, method to be used,input parameters
output: target varable value for given input parameters.
method= ensemble[BAG-[HOMO/HETRO],BOOST[HOMO/HETRO],STACK[HOMO/HETRO]],LDA 
When you start game tell which model/technique to use.
game will send command : [init BAG-0/BAG-1/BOOST-0/BOOST-1/STACK-0/STACK-1/LDA/...,]
"""
from Config import Config

def BuildModel(aimodel: str):
    global cfg
    cfg=Config(aimodel,fname="../data/GAPCK.csv")

def getColumnName():
    return cfg.ColumnName

def GetPrediction(attributes:str ):
    return cfg.predict(attributes,cfg.model,cfg.ColumnName)