from src.data_pipeline import DataPipeline
from src.model_pipeline import ModelPipeline

data_obj = DataPipeline()
data_obj.load_data('data/Customertravel.csv')
train_data, val_data, test_data = data_obj.split_data()

model_obj = ModelPipeline()
model_obj.fit(train_data, val_data)
model_obj.evaluate(test_data)