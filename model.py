import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv('C:/Users/nived/OneDrive/Desktop/iotanalyst/file.csv')

data

# Split data into features and labels
X = data.drop('class', axis=1)
y = data['class']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

len(X_train)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

train_pred=rf.predict(X_train)
accuracy2=accuracy_score(y_train,train_pred)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(f"Accuracy2: {accuracy2:.2f}")
# saving the model
import pickle
pickle_out = open("rf.pkl", mode = "wb")
pickle.dump(rf, pickle_out)
pickle_out.close()