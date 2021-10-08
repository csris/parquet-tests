import pandas as pd


iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris.to_parquet('iris.parquet')
