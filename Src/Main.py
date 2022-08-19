import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, PowerTransformer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, cohen_kappa_score

import pickle
import yaml

with open("../params.yaml", "r") as file:
	config = yaml.safe_load(file)

with open(config["Data"]["CleanMVPs"], "r", encoding = "utf-8") as file:
	mvps = pd.read_csv(file)
		  
mvps = mvps.drop(columns = ["Player", "Tm", "First", "Pts Won", "Pts Max", "Year"])

state = config["Random"]["State"]
size = config["Test_Size"]["Standard"]

mvps_rank = mvps[["Rank", "WS/48", "Stats/M"]]
		  
rank_X = mvps_rank.drop(columns = "Rank")
rank_y = mvps_rank["Rank"]

rank_X_train, rank_X_test, rank_y_train, rank_y_test = train_test_split(rank_X, rank_y, test_size = size, random_state = state)
		  
with open(config["Transformers"]["Rank"], "rb") as file:
	rank_pt = pickle.load(file)
		  
rank_X_train_pt = rank_pt.transform(rank_X_train)
rank_X_train_pt = pd.DataFrame(rank_X_train_pt, columns = rank_X_train.columns, index = rank_X_train.index)

rank_X_test_pt = rank_pt.transform(rank_X_test)
rank_X_test_pt = pd.DataFrame(rank_X_test_pt, columns = rank_X_test.columns, index = rank_X_test.index)
		  
with open(config["Scalers"]["Rank"], "rb") as file:
	rank_scaler = pickle.load(file)

rank_X_train_pt_mm = rank_scaler.transform(rank_X_train_pt)
rank_X_train_pt_mm = pd.DataFrame(rank_X_train_pt_mm, columns = rank_X_train_pt.columns, index = rank_X_train_pt.index)

rank_X_test_pt_mm = rank_scaler.transform(rank_X_test_pt)
rank_X_test_pt_mm = pd.DataFrame(rank_X_test_pt_mm, columns = rank_X_test_pt.columns, index = rank_X_test_pt.index)
		  
with open(config["Models"]["Rank"], "rb") as file:
	rank_lr = pickle.load(file)

rank_train_y_pred = rank_lr.predict(rank_X_train_pt_mm)
rank_test_y_pred = rank_lr.predict(rank_X_test_pt_mm)

print("First Model Train Score: {:.2f}".format(r2_score(rank_y_train, rank_train_y_pred),2))
print("First Model Test Score: {:.2f}".format(r2_score(rank_y_test, rank_test_y_pred),2))

mvps_share = mvps[["Share", "WS/48", "Stats/M"]]

share_X = mvps_share.drop(columns = "Share")
share_y = mvps_share["Share"]

share_X_train, share_X_test, share_y_train, share_y_test = train_test_split(share_X, share_y, test_size = size, random_state = state)

with open(config["Transformers"]["Share"], "rb") as file:
	share_pt = pickle.load(file)

share_X_train_pt = share_pt.transform(share_X_train)
share_X_train_pt = pd.DataFrame(share_X_train_pt, columns = share_X_train.columns, index = share_X_train.index)

share_X_test_pt = share_pt.transform(share_X_test)
share_X_test_pt = pd.DataFrame(share_X_test_pt, columns = share_X_test.columns, index = share_X_test.index)

with open(config["Scalers"]["Share"], "rb") as file:
	share_scaler = pickle.load(file)

share_X_train_pt_mm = share_scaler.transform(share_X_train_pt)
share_X_train_pt_mm = pd.DataFrame(share_X_train_pt_mm, columns = share_X_train_pt.columns, index = share_X_train_pt.index)

share_X_test_pt_mm = share_scaler.transform(share_X_test_pt)
share_X_test_pt_mm = pd.DataFrame(share_X_test_pt_mm, columns = share_X_test_pt.columns, index = share_X_test_pt.index)

		  
with open(config["Models"]["Share"], "rb") as file:
	share_lr = pickle.load(file)

share_train_y_pred = share_lr.predict(share_X_train_pt_mm)
share_test_y_pred = share_lr.predict(share_X_test_pt_mm)

print("Second Model Train Score: {:.2f}".format(r2_score(share_y_train, share_train_y_pred),2))
print("Second Model Test Score: {:.2f}".format(r2_score(share_y_test, share_test_y_pred),2))

mvps["Top3"] = mvps["Rank"] <= 3

top3_X = mvps[["WS/48", "Stats/M"]]
top3_y = mvps["Top3"]

top3_X_train, top3_X_test, top3_y_train, top3_y_test = train_test_split(top3_X, top3_y, test_size = size, random_state = state)

with open(config["Transformers"]["Top3"], "rb") as file:
	top3_pt = pickle.load(file)

top3_X_train_pt = top3_pt.transform(top3_X_train)
top3_X_train_pt = pd.DataFrame(top3_X_train_pt, columns = top3_X_train.columns, index = top3_X_train.index)

top3_X_test_pt = top3_pt.transform(top3_X_test)
top3_X_test_pt = pd.DataFrame(top3_X_test_pt, columns = top3_X_test.columns, index = top3_X_test.index)

with open(config["Scalers"]["Top3"], "rb") as file:
	top3_scaler = pickle.load(file)

top3_X_train_pt_mm = top3_scaler.transform(top3_X_train_pt)
top3_X_train_pt_mm = pd.DataFrame(top3_X_train_pt_mm, columns = top3_X_train_pt.columns, index = top3_X_train_pt.index)

top3_X_test_pt_mm = top3_scaler.transform(top3_X_test_pt)
top3_X_test_pt_mm = pd.DataFrame(top3_X_test_pt_mm, columns = top3_X_test_pt.columns, index = top3_X_test_pt.index)

with open(config["Models"]["Top3"], "rb") as file:
	top3_lr = pickle.load(file)

top3_lr_y_train_pred = top3_lr.predict(top3_X_train_pt_mm)
top3_lr_y_test_pred = top3_lr.predict(top3_X_test_pt_mm)

print("Third Model Train Kappa Score: {:.2f}".format((cohen_kappa_score(top3_y_train, top3_lr_y_train_pred))))
print("Third Model Test Kappa Score: {:.2f}".format(cohen_kappa_score(top3_y_test, top3_lr_y_test_pred)))

mvps["Top5"] = mvps["Rank"] <= 5

top5_X = mvps[["WS/48", "Stats/M"]]
top5_y = mvps["Top5"]

top5_X_train, top5_X_test, top5_y_train, top5_y_test = train_test_split(top5_X, top5_y, test_size = size, random_state = state)

with open(config["Transformers"]["Top5"], "rb") as file:
	top5_pt = pickle.load(file)

top5_X_train_pt = top5_pt.transform(top5_X_train)
top5_X_train_pt = pd.DataFrame(top5_X_train_pt, columns = top5_X_train.columns, index = top5_X_train.index)

top5_X_test_pt = top5_pt.transform(top5_X_test)
top5_X_test_pt = pd.DataFrame(top5_X_test_pt, columns = top5_X_test.columns, index = top5_X_test.index)

with open(config["Scalers"]["Top5"], "rb") as file:
	top5_scaler = pickle.load(file)

top5_X_train_pt_mm = top5_scaler.transform(top5_X_train_pt)
top5_X_train_pt_mm = pd.DataFrame(top5_X_train_pt_mm, columns = top5_X_train_pt.columns, index = top5_X_train_pt.index)

top5_X_test_pt_mm = top5_scaler.transform(top5_X_test_pt)
top5_X_test_pt_mm = pd.DataFrame(top5_X_test_pt_mm, columns = top5_X_test_pt.columns, index = top5_X_test_pt.index)

with open(config["Models"]["Top5"], "rb") as file:
	top5_lr = pickle.load(file)

top5_lr_y_train_pred = top5_lr.predict(top5_X_train_pt_mm)
top5_lr_y_test_pred = top5_lr.predict(top5_X_test_pt_mm)

print("Fourth Model Train Kappa Score: {:.2f}".format(cohen_kappa_score(top5_y_train, top5_lr_y_train_pred)))
print("Fourth Model Test Kappa Score: {:.2f}".format(cohen_kappa_score(top5_y_test, top5_lr_y_test_pred)))

with open(config["Data"]["MVPs_X"], "r", encoding = "utf-8") as file:
	mvps_X = pd.read_csv(file)
	
with open(config["Data"]["MVPs_y"], "r", encoding = "utf-8") as file:
	mvps_y = pd.read_csv(file)
	
size2 = config["Test_Size"]["MVPs"]
	
mvps_X_train, mvps_X_test, mvps_y_train, mvps_y_test = train_test_split(mvps_X, mvps_y, test_size = size2, random_state = state)

with open(config["Transformers"]["MVPs"], "rb") as file:
	mvps_pt = pickle.load(file)

mvps_X_train_pt = mvps_pt.transform(mvps_X_train)
mvps_X_train_pt = pd.DataFrame(mvps_X_train_pt, columns = mvps_X_train.columns, index = mvps_X_train.index)

mvps_X_test_pt = mvps_pt.transform(mvps_X_test)
mvps_X_test_pt = pd.DataFrame(mvps_X_test_pt, columns = mvps_X_test.columns, index = mvps_X_test.index)

with open(config["Models"]["MVPs"], "rb") as file:
	mvps_lr = pickle.load(file)

mvps_y_train_pred = mvps_lr.predict(mvps_X_train_pt)
mvps_y_test_pred = mvps_lr.predict(mvps_X_test_pt)

print("Fifth Model Train Score: {:.2f}".format(r2_score(mvps_y_train, mvps_y_train_pred)))
print("Fifth Model Train Score: {:.2f}".format(r2_score(mvps_y_test, mvps_y_test_pred)))