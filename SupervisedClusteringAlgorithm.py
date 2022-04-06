# Tyler Koenig
# CS379 Machine Learning
# November 3, 2021
# Description: This algorithm will predict if a passenger will survive on the titanic
# Libraries
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
titanic = sns.load_dataset('titanic')

# Print first 10 rows
print(titanic.head(10))

# Print size of dataset
print(titanic.shape)

# Get a count of survivors and deaths
print(titanic['survived'].value_counts())

# Check survival rate by sex and class
print(titanic.pivot_table('survived', index='sex', columns='class'))

# Drop unnecessary data
titanic = titanic.drop(['deck', 'embark_town', 'alive', 'class', 'alone', 'adult_male', 'who'], axis=1)

# Remove rows with missing values
titanic = titanic.dropna(subset=['embarked', 'age'])

# Print new size
print(titanic.shape)

# Show unique values
print(titanic['sex'].unique())
print(titanic['embarked'].unique())

labelencoder = LabelEncoder()

# Encode sex
titanic.iloc[:, 2] = labelencoder.fit_transform(titanic.iloc[:, 2].values)

# Encode embarked
titanic.iloc[:, 7] = labelencoder.fit_transform(titanic.iloc[:, 7].values)

# Print the translated values
print(titanic['sex'].unique())
print(titanic['embarked'].unique())

# Split dataset
X = titanic.iloc[:, 1:8].values
Y = titanic.iloc[:, 0].values

# Split into testing and training sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Implement Random Forest
forest = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
forest.fit(X_train, Y_train)

# Display accuracy
print('Random Forest Classifier Training Accuracy:', forest.score(X_train, Y_train))
