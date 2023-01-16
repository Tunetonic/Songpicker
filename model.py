from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import os

train_data_file_path = os.path.join(os.path.dirname(__file__), "train-data", "train_data.csv")
test_data_file_path = os.path.join(os.path.dirname(__file__), "train-data", "train_data.csv")

train_data = pd.read_csv(train_data_file_path, index_col=False)
test_data = pd.read_csv(test_data_file_path, index_col=False)

X_train, X_test, y_train, y_test = train_test_split(train_data, test_data, test_size=0.3) # 70% training and 30% test

vect = CountVectorizer()
X = vect.fit_transform(list(train_data.columns))
y = vect.transform(train_data)

model = SVC()

model.fit(X, y)

y_pred = model.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
