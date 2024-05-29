import array
import operator
import pandas as pd
import numpy as np
from pandas import read_csv
from pandas import DataFrame
import sklearn.metrics as skm
import sklearn.ensemble as ske
from sklearn.feature_selection import RFE
from sklearn import model_selection as ms
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler

data=pd.read_csv("attributes_nef_int.csv")
arr=data.values
# below are the features
dat=arr[:,1:18]


#Extract labels
label=arr[:,18]

#Splitting data- 70-30 split, scoring based on accuracy
valid_size=0.30
seed=7
train,test,train_label,test_label=ms.train_test_split(dat,label,test_size=valid_size,random_state=seed)
scoring='accuracy'


#Hyperprameter optimisation, model training
params = {'max_depth' : [9],'n_estimators': [300],'min_samples_split': [3],'min_samples_leaf': [5]}
rf = ske.RandomForestClassifier(bootstrap=True,random_state = None, n_jobs=-1,max_features='auto', max_leaf_nodes=None,)
model = GridSearchCV(rf, params ,cv = 5,n_jobs=-1)
model.fit(train, train_label)
print(model.best_params_)
print(model.best_score_)  

# testing accuracy
predict_test = model.predict(test)
print(skm.accuracy_score(predict_test, test_label))
