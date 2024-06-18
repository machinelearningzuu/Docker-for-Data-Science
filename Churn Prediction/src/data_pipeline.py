import pandas as pd
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split

class DataPipeline:

    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)

    def split_data(self):
        X = self.data.drop(columns=['Target'],axis=1)
        y = self.data['Target']
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=123)
        X_train, X_val, y_train, y_val = train_test_split(X_train,y_train,test_size=0.2,random_state=123)
        train_data = Pool(data=X_train,label=y_train,cat_features=[1,2,4,5])
        val_data = Pool(data=X_val,label=y_val,cat_features=[1,2,4,5])
        test_data = Pool(data=X_test,label=y_test,cat_features=[1,2,4,5])
        return train_data, val_data, test_data
    