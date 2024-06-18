import pickle
from catboost import CatBoostClassifier
from sklearn.metrics import recall_score, precision_score

class ModelPipeline:
    def __init__(self):
        self.model = CatBoostClassifier(
                                        depth=4,
                                        n_estimators=500,
                                        learning_rate=0.1,
                                        loss_function='Logloss',
                                        random_seed=123,
                                        verbose=True
                                        )
        self.model_path = 'artifacts/model.pkl'     

    def fit(
            self, 
            train_data, 
            val_data
            ):
        self.model.fit(
                        train_data,
                        eval_set=val_data
                        )
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.model, f)
        
    def predict(
                self, 
                data
                ):
        return self.model.predict(data)
    
    def evaluate(
                self, 
                test_data
                ):
        y_pred = self.model.predict(test_data)
        y_true = test_data.get_label()
        
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        
        print(f'Precision: {precision}')
        print(f'Recall: {recall}')