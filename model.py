# Accuracy : 0.8561066200568058
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import os, time
from scipy import stats

os.chdir(r"C:\Users\raveendra\Documents\GitHub\pesuio_final_assignment\dataset")
ds = pd.read_csv('combined_csv.csv')
print(ds.count().sort_values())
ds = ds.drop(columns=['Sunshine','Evaporation','Cloud3pm','Cloud9am','Location','RISK_MM','Date','WindGustDir','WindDir9am','WindDir3pm'],axis=1)
ds[['RainTomorrow','RainToday']] = ds[['RainTomorrow','RainToday']].replace({'No':0,'Yes':1})
ds = ds.dropna(how='any')

# Removing Outliers in my dataset
z = np.abs(stats.zscore(ds._get_numeric_data()))
ds= ds[(z < 3).all(axis=1)]

# Pre processing the data
scale = sk.preprocessing.MinMaxScaler()
scale.fit(ds)
ds = pd.DataFrame(scale.transform(ds), index=ds.index, columns=ds.columns)

# Sorting the features and lables
y = ds.RainTomorrow
x = ds.drop(['RainTomorrow'], axis=1)

# Applying Logistic Regression Algorithm

t0=time.time()
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2)
reg = LogisticRegression(random_state=0,max_iter = 9999)
reg.fit(xtrain,ytrain)
ypred = reg.predict(xtest)
acc = accuracy_score(ytest,ypred)
print('Accuracy :',acc)
print('Time taken :' , time.time()-t0)