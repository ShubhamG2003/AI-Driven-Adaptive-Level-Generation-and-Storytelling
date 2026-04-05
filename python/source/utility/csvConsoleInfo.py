"""
A small utility program to get basic information about dataframe
like total memory consumed, column name and type , number of unique 
values ,min and max values per column etc.
Useful when you want to see memory consumed if all column are read. 
"""

import pandas as pd


# ------------------------------------------------------------------------------
def ColumnInformation(dFrame: pd.DataFrame) -> None:
    print("-" * 50)
    for colname in dFrame.columns:
        print(f"Column Name: {colname}")
        print(dFrame[colname].describe(percentiles=[]).to_string())
        print(f"Memory Usage : {dFrame[colname].memory_usage(deep=True)/1024:.2f} KB")
        print(f"Top five values by count()")
        df = dFrame.groupby(colname, observed=False)[colname].count().nlargest(5)
        print(df.to_string())
        print("-" * 50)
    return


# ------------------------------------------------------------------------------
def DataFrameInformation(dFrame: pd.DataFrame, summaryonly: bool = False,fname="../../data/GameAttributes.csv") -> None:
    numAttributes = len(dFrame.columns)
    numRecords = len(dFrame)
    numMissing = dFrame.isnull().sum().sum()
    numDuplicated = dFrame.duplicated().sum()
    memSize = dFrame.memory_usage(index=True, deep=True).sum()
    print("-"*60)
    print(f" Summary for data file [{fname}] ")
    print("-"*60)
    print(f"Number of Attributes         {numAttributes}")
    print(f"Number of Records are        {numRecords}")
    print(f"Total memory size            {memSize/(1024*1024):.2f} MB")
    print(f"Avg record size in memory    {(memSize/numRecords):.0f} Bytes")
    print(f"Number of missing cells      {numMissing}")
    print(f"Percent of missing cells     {(numMissing/numRecords)*100}")
    print(f"Number of duplicate Records  {numDuplicated}")
    print(f"Percent of duplicate Records {(numDuplicated/numRecords)*100}\n")
    colDataTypes = dFrame.dtypes
    print(f"Attribute Name and Type:\n{colDataTypes.to_string()}\n")
    if summaryonly == False:
        ColumnInformation(dFrame)
    return


# ------------------------------------------------------------------------------
def csvInfo(fname="../../data/GameAttributes.csv"):
    dFrame = pd.read_csv(fname)    
    DataFrameInformation(dFrame,False,fname)
    return


# ------------------------------------------------------------------------------
csvInfo()
