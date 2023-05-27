def predict(id):
    return True
    import numpy as np
    import pandas as pd

    from sklearnex import patch_sklearn

    # Patch Scikit Learn
    patch_sklearn()

    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_error

    def f(x):
        try:
            return float(x)
        except:
            return 0

    train = pd.read_csv("Datasets/user_books.csv")
    test=pd.read_csv("Datasets/general_books.csv")

    unwanted_columns = ['title', 'language','isbn','coverImg']
    columns = list(x for x in list(test) if x not in unwanted_columns)

    test = test[columns]
    for column in columns:
        test[column] = test[column].apply(f)
    test = test.replace(np.nan, 0)
    test=test.drop('rating', axis=1)

    train = train[train['UserId'] == id]
    train = train[columns]
    for column in columns:
        train[column] = train[column].apply(f)
    train = train.replace(np.nan, 0)

    train_X= train.drop('rating', axis = 1)
    train_y=train["rating"]

    model = RandomForestRegressor(random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(test)
    print(preds_val)

if __name__ == '__main__':
    # This code block will only run when the file is executed directly, not when imported
    # You can add any test code or additional functionality here
    pass