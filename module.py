import numpy as np
import pandas as pd

from sklearnex import patch_sklearn

# Patch Scikit Learn
patch_sklearn()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def predict(id):

    def f(x):
        try:
            return float(x)
        except:
            return 0

    train = pd.read_csv("Datasets/user_books.csv")
    test = pd.read_csv("Datasets/general_books.csv")

    unwanted_columns = ['title', 'language','isbn','coverImg']
    columns = list(x for x in list(test) if x not in unwanted_columns)

    test_x = test[columns]
    for column in columns:
        test_x[column] = test_x[column].apply(f)
    test_x = test_x.replace(np.nan, 0)
    test_x=test_x.drop('rating', axis=1)

    train_X = train[train['UserId'] == id]
    train_X = train_X[columns]
    for column in columns:
        train_X[column] = train_X[column].apply(f)
    train_X = train_X.replace(np.nan, 0)

    train_y = train_X["rating"]
    train_X = train_X.drop('rating', axis = 1)

    model = RandomForestRegressor(random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(test_x)
    output = test
    output["rating"] = preds_val
    output = output.merge(train[['title']], on='title', how='left', indicator=True)
    output = output[output['_merge'] == 'left_only']
    output = output.sort_values('rating', ascending=False)
    print(list(output.head()['title']))

if __name__ == '__main__':
    # This code block will only run when the file is executed directly, not when imported
    # You can add any test code or additional functionality here
    pass
predict(31415)