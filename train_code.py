import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import utils
from test_code import predictStrokeLabel
from PreprocessingCodes.showpoints import showpoints
from PreprocessingCodes.interpolation import interpolation
from FeatureExtractionCodes.features import features

def getFeatures(folderPath, filename):
    d = showpoints('Original Plot', filename, folderPath)
    print(d)
    d = interpolation(d)
    final_features = features(d)
    return final_features

### Training Part Starts ### 
x=pd.read_csv("training_dataset.csv")
c = np.array(x)
y = c[:,0]
x.drop(["Class"], axis=1,inplace=True)
a=np.array(x)


lab_enc = preprocessing.LabelEncoder()

clf = SVC(C=1.0, kernel='poly',degree=3, gamma=2)
clf.fit(x, y) 
### Training Part Ends ###

### Testing Part Starts ###
folderPath = input("Enter folder path: ")
fileName = input("Enter file name: ")

features = getFeatures(folderPath, fileName)
result = clf.predict([features])
print(int(result[0]))
### Testing Part Ends ###

print(clf.score(x,y))







