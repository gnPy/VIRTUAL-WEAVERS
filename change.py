""" The Following program uses the genre column to produce columns for each genre"""

import pandas as pd

def str_to_dict(string):
    string = ''.join(x for x in string if x.isalpha() or x==',')
    l = [x for x in string.split(',') if x]
    out = {}
    for i in l:
        out[i]=1
    return out

df=pd.read_csv("Datasets/details.csv")
df=pd.concat([df, df['genres'].apply(str_to_dict).apply(pd.Series).fillna(0).astype(int)], axis=1)
df.to_csv("Datasets/general_books")