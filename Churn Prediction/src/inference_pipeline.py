import pickle 
import pandas as pd 

class InferencePipeline:
    def __init__(self):
        self.model_path = 'artifacts/model.pkl'
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
    
    def format_data(
                    self, 
                    data_json,
                    columns = [
                                'Age',
                                'FrequentFlyer',
                                'AnnualIncomeClass',
                                'ServicesOpted',
                                'AccountSyncedToSocialMedia',
                                'BookedHotelOrNot'
                                ]
                    ):
        data_df = pd.DataFrame(data_json, index=[0])
        data_df = data_df[columns]
        return data_df
    
    def predict(
                self, 
                data
                ):
        data = self.format_data(data)
        p = self.model.predict(data)
        p = 'CHURN' if p[0] == 1 else 'NOT-CHURN'
        return p