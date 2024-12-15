import os

os.system("python src/data_ingestion.py")
print("Data ingestion run")

os.system("python src/data_preprocessing.py")
print("Data data_preprocessing run")

os.system("python src/feature_engineering.py")
print("feature_engineering run")

os.system("python src/model_building.py")
print("model_building run")

os.system("python src/model_evaluation.py")
print("model_evaluation run")
