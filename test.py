# coding: utf-8 aaa
import pandas as pd
pd.read_excel(C:\Users\viktoras.valiokas\Desktop\Python projects\Hearthstone-Card-Value-Predictions\cards.xlsx)
pd.read_excel(cards.xlsx)
pd.read_excel("cards.xlsx")
get_ipython().system('pip install xlrd')
df = pd.read_excel("cards.xlsx")
df
df
df.columns
df.set
df.unique()
df.set.unique()
get_ipython().run_line_magic('save', 'testfile n1-n20')
df.set.value_counts()
df.set.value_counts().head(5)
df.set.value_counts().tail(3)
df.set.value_counts().mean
df.set.value_counts().mean()
df.set.value_counts().min()
df.set.value_counts().max()
df.set.value_counts().idxmax()
df
df.query("set = 'DEMON_HUNTER_INITIATE'")
df.query("set == 'DEMON_HUNTER_INITIATE'")
sdf = df.query("set == 'DEMON_HUNTER_INITIATE'")
sdf
sdf.head
sdf.head()
sdf.sort_by("cost")
sdf.sort_values(by = "cost")
sdf.sort_values(by = "cost").dropna()
sdf.sort_values(by = "cost").dropna(subset=["cost"])
sdf.sort_values(by = "cost", ascending = false).dropna(subset=["cost"])
sdf.sort_values(by = "cost", ascending = False).dropna(subset=["cost"])
get_ipython().run_line_magic('save', 'test.py 1-30')
get_ipython().run_line_magic('save', 'test.py 1-50')
