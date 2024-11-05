import pandas as pd
from collections import Counter
from imblearn.over_sampling import SMOTE

def smote(X_train, y_train):
    con = Counter(y_train)
    plot1 = print('Przed',con)
    smote = SMOTE(random_state=42)
    X_train_sm, y_train_sm = smote.fit_resample(X_train,y_train)
    con1 = Counter(y_train_sm)
    plot2 = print('Po', con1)
    plot3  = pd.Series(y_train_sm).value_counts().plot.bar()
    return plot1, plot2, plot3 
