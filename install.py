import xgboost as xgb
import pandas as pd
import numpy as np


dtrain = pd.read_csv("./data/ssh_logs/SSH.csv")

dtrain.head()
