import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Testing Tools
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

dataset = pd.read_csv(r"C:\Users\Tyler\Downloads\vgsales.csv\vgsales.csv")

# Ignore invalid characters
# bytes.decode(dataset, encoding="utf-8", errors="ignore")

# Drop irrelevant columns
# dataset.drop(columns=['ID', 'name', 'category', 'main_category', 'currency', 'deadline', 'launched', 'pledged',
                      # 'country', 'usd pledged', 'usd_pledged_real', 'usd_goal_real'], inplace=True)

# Remove invalid values

# Training data
x = dataset.iloc[:, 0:6]
# Testing data
y = dataset.iloc[:, 6]

# Set size of test data
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.3)

# Setting the K variable and calculating Euclidean Distance
classifier = KNeighborsClassifier(n_neighbors=569, p=3, metric='euclidean')

# Fit model
classifier.fit(x_train, y_train)

# Predict test set results
y_prediction = classifier.predict(x_test)

# Evaluate Model
cm = confusion_matrix(y_test, y_prediction)
print(cm)

# Print Output
print("F1 score: " + f1_score(y_test, y_prediction))
print("Accuracy score: " + accuracy_score(y_test, y_prediction))
