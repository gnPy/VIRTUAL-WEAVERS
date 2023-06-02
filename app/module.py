import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from sklearnex import patch_sklearn

# Patch Scikit Learn
patch_sklearn()

def f(x):
    try:
        num = float(x)
    except:
        return 0
    if num%1==0:
        return int(x)
    return float(x)
    
def predict(id):
    user_books = pd.read_csv("Datasets/user_books.csv")
    general_books = pd.read_csv("Datasets/details.csv", low_memory=False)

    if id not in set(user_books['UserId']):
        return None

    unwanted_columns = ['author', 'description', 'language','isbn','coverImg', 'title', 'ratingsByStars']
    columns=list(general_books)

    user_books = user_books.loc[user_books['UserId'] == id, :]
    user_books = user_books[["title", "UserRating"]]
    books = general_books.loc[general_books['title'].isin(user_books['title'])]
    books = pd.merge(books, user_books, on="title")

    train = books.drop(unwanted_columns, axis=1)
    test_X = general_books.drop(unwanted_columns, axis=1)
    
    for column in list(test_X):
        test_X[column] = test_X[column].apply(f)
        train[column] = train[column].apply(f)
            
    train_y = train['UserRating']
    train_X = train.drop('UserRating', axis=1)

    model = RandomForestRegressor()
    print(train_X)
    model.fit(train_X, train_y)
    preds_val = model.predict(test_X)

    output = general_books
    output["rating"] = preds_val
    output = output.merge(books[['title']], on='title', how='left', indicator=True)
    output = output[output['_merge'] == 'left_only']
    output = output.sort_values('rating', ascending=False)
    l=list(output.head(8)['title'])
    return l

def get_details(name_list):
    original_df = pd.read_csv("Datasets/details.csv", low_memory=False)
    filtered_df = original_df[original_df['title'].isin(name_list)]
    temp=filtered_df[['title','coverImg','rating','language']]
    dictionary=dict()
    for column in temp:
        dictionary[column] = list(temp[column])
    return dictionary

def get_row_as_dict(df, name):
    row = df.loc[df['title'] == name]
    if len(row) > 0:
        return row.iloc[0].to_dict()
    else:
        return None

if __name__ == '__main__':
    # This code block will only run when the file is executed directly, not when imported
    # You can add any test code or additional functionality here
    pass