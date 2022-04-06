# Tyler Koenig
# CS379 Machine Learning
# November 15, 2021
# Description: This algorithm will detect credit card fraud

# Import Libraries
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import sklearn
from scipy.io import arff
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

# Print library versions
print('Python: {}'.format(sys.version))
print('NumPy: {}'.format(np.__version__))
print('Pandas: {}'.format(pd.__version__))
print('MatPlotLib: {}'.format(matplotlib.__version__))
print('Seaborn: {}'.format(sns.__version__))
print('SciPy: {}'.format(scipy.__version__))
print('SKLearn: {}'.format(sklearn.__version__))

# Load the dataset
data = arff.loadarff(r'C:\Users\Tyler\Downloads\creditfruad original.arff')

# Load as pandas dataframe
df = pd.DataFrame(data[0])

# Explore dataframe
print(df.columns)

# Print dataframe size
print(df.shape)

# Replace "good" and "bad" with numeric data
# df['class'] = df['class'].map({'good': 0, 'bad': 1})

# Plot and show histograms
df.hist()
plt.show()

# Define Fraud and Valid transactions
Fraud = 300
Valid = 700

# Define and print fraction of outliers
outlierFraction = Fraud / float(Valid)
print(outlierFraction)

# Print number of Fraudulent and Valid cases
print(df["class"].value_counts())

# Correlation Matrix
corrmat = df.corr()
fig = plt.figure(figsize=(12, 9))

# Heat Map
sns.heatmap(corrmat, vmax=0.8, square=True)
plt.show()

# Get list of columns
columns = df.columns.tolist()

# Remove class column
columns = [c for c in columns if c not in ['class']]

# Store prediction variable
target = 'class'

# Split dataset into X and Y sets
X = df[columns]
Y = df[target]

# Print shapes of X and Y
print(X.shape)
print(Y.shape)

# Define a random state
state = 1

# Define the outlier detection methods
classifiers = {
    "Isolation Forest": IsolationForest(max_samples=len(X),
                                        contamination=outlierFraction,
                                        random_state=state),
    "Local Outlier Factor": LocalOutlierFactor(
        n_neighbors=19,
        contamination=outlierFraction)
}

# Fit the model
n_outliers = Fraud

for i, (clf_name, clf) in enumerate(classifiers.items()):

    # Fit the data and detect outliers
    if clf_name == "Local Outlier Factor":
        y_pred = clf.fit_predict(X)
        scores_pred = clf.negative_outlier_factor_
    else:
        clf.fit(X)
        scores_pred = clf.decision_function(X)
        y_pred = clf.predict(X)

    # Reshape the prediction values to 0 for Valid and 1 for Fraud
    y_pred[y_pred == 1] == 0
    y_pred[y_pred == -1] == 1

    n_errors = (y_pred != Y).sum()

    # Run classification metrics
    print('{}: {}'.format(clf_name, n_errors))
    print("Accuracy: ", accuracy_score(Y, y_pred))
    print(classification_report(Y, y_pred))
