# Tyler Koenig
# CS379 Machine Learning
# November 9, 2021
# Description: This algorithm will predict the type of iris based on measurements

# Libraries
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# Load dataset
iris = sns.load_dataset('iris')

# Print first 10 rows
print(iris.head(10))

# Print size of dataset
print(iris.shape)

# Get a count of species used in dataset
print(iris['species'].value_counts())

# Split dataset
X = iris.iloc[:, 0:4].values
Y = iris.iloc[:, 4].values

# Split into testing and training sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Run Random Forest
forest = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
forest.fit(X_train, Y_train)

# Run K Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=2, metric='minkowski', p=2)
knn.fit(X_train, Y_train)

# Run Naive Bayes
gauss = GaussianNB()
gauss.fit(X_train, Y_train)

# Display accuracies
print('Random Forest Accuracy:', forest.score(X_train, Y_train))
print('K Nearest Neighbors Accuracy:', knn.score(X_train, Y_train))
print('Naive Bayes Accuracy:', gauss.score(X_train, Y_train))
