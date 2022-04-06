# Big Data Analytics: Tyler Koenig

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

import numpy as np
import random
import math
import operator

# Build Spark Session
spark = SparkSession.builder.master("local[*]").appName("ETL Pipeline").getOrCreate()

# Set Logging Level to WARN
spark.sparkContext.setLogLevel("WARN")

# Clean data
sourceDataFile = r"C:\Users\Tyler\Desktop\zipCode\Demographic_Statistics_By_Zip_Code.csv"

# Define CSV input schema
schema = StructType([
    StructField("JURISDICTION NAME", IntegerType()),
    StructField("COUNT PARTICIPANTS", IntegerType()),
    StructField("COUNT FEMALE", IntegerType()),
    StructField("COUNT MALE", IntegerType()),
])

# Have spark read the csv file
data = spark.read.csv(sourceDataFile, schema=schema).cache()


# Turn zero values into Nulls
zerosNotAccepted = ['COUNT PARTICIPANTS']

for column in zerosNotAccepted:
    data[column] = data[column].replace(0, np.NaN)
    mean = int(data[column].mean(skipna=True))
    data[column] = data[column].replace(np.NaN, mean)


# Filter any NULL values
df = data.filter("integer is not NULL")

dfCount = df.count
print("Data points remaining after removing nulls: {}".format(dfCount))

print("Removed {} nulls".format(data - dfCount))


# Write to postgres database
def writeDFToTable(dfWriter, table):
    jdbcURL = "jdbc:postgresql://0.0.0.0:5432/postgres"
    node = "overwrite"
    properties = {"user": "postgres",
                  "password": "password",
                  "driver": "org.postgres.Driver"}

    dfWriter.jdbc(jdbcURL, table, node, properties)


# Split into training set and test set
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = data.DictReader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


# Calculate Euclidean Distance
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# Calculate Neighbors
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# Predict response based on neighbors
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=lambda vote: [1], reverse=True)
    return sortedVotes[0][0]


# Calculate accuracy of predictions
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] is predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


# Driver Code
print('Results: ')
trainingSet = []
testSet = []
split = 0.70

print('Train Set: ' + repr(len(trainingSet)))
print('Test Set: ' + repr(len(testSet)))

# Make prediction
predictions = []
k = 11

for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)

accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')

