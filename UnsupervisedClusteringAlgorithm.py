# Tyler Koenig
# CS379 Machine Learning
# November 3, 2021
# Description: This algorithm will predict if a passenger will survive on the titanic
# Libraries
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

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

# Implement K Means algorithm
kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10, random_state=0)

# Assign visualization to variable
label = kmeans.fit_predict(titanic)

# Print results
print(label)
