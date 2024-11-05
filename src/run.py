import dataset
import smote

# variables
ds = "D:/ml/xgboost-main/data/ssh_logs/SSH.csv"

dataset.df(ds)  # dataset create df on output

smote.smote(X_train, y_train)  # create SMOTE
