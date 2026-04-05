"""
This program will display 'GamesAttributes.csv' grahically for
quick understanding of data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import seaborn as sns


def DataFrameDisplay(dFrame:pd.DataFrame,fname:str):
    numAttributes = len(dFrame.columns)
    numRecords = len(dFrame)
    
    #for i in range(numAttributes-1):
    dFrame.plot.pie (y=dFrame.columns[0])
    plt.show()
    return

# ------------------------------------------------------------------------------
def csvGraphInfo(fname="../../data/GameAttributes.csv"):
    dFrame = pd.read_csv(fname)     
    DataFrameDisplay(dFrame,fname)
    return


# ------------------------------------------------------------------------------
csvGraphInfo()
