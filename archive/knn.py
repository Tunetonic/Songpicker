from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import roc_auc_score
import joblib
import pandas as pd
import os

train_data_file_path = os.path.join(os.path.dirname(__file__), "data", "titled_train_data.csv")
train_data = pd.read_csv(train_data_file_path, index_col=False)

X = train_data['genre'] 
y = train_data['like/dislike']

vect = CountVectorizer(max_features=len(X))
X2 = vect.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.2, random_state=1)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = roc_auc_score(y_test, y_pred)
print(accuracy)

model_file_save_path = os.path.join(os.path.dirname(__file__), "models", "knn_model.sav")
joblib.dump(knn, model_file_save_path)