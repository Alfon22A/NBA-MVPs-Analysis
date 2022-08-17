import pickle
import yaml

with open("../params.yaml", "r") as file:
	config = yaml.safe_load(file)

with open(config["Scalers"]["rank_scaler"], "rb") as file:
	scaler = pickle.load(file)