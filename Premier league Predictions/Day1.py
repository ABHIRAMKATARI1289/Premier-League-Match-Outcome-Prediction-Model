import pandas as pd 

df = pd.read_csv('premier-league-matches.csv')
print(df.shape)
print(df.head(7))
print(df.dtypes)
print(df.isnull().sum())