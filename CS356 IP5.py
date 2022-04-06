# CS356 Big Data Analytics: Tyler Koenig

import csv
import random
import math
import operator
import numpy as np

with open(r"C:\Users\Tyler\Downloads\Demographic_Statistics_By_Zip_Code.csv") as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))

# Preprocessing and Cleaning
# Replace zeros with null values
zerosNotAccepted = ['COUNT PARTICIPANTS']

for column in zerosNotAccepted:
    csvfile[column] = csvfile[column].replace(0, np.NaN)
    mean = int(csvfile[column].mean(skipna=True))
    csvfile[column] = csvfile[column].replace(np.NaN, mean)

# Drop irrelevant columns
csvfile.drop(
    columns=['D', 'F', 'G', 'H', 'I ', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
             'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ',
             'AR', 'AS', 'AT'], inplace=True)


# Split into training set and test set
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.DictReader(csvfile)
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


# Prepare data
print('Results: ')
trainingSet = []
testSet = []
split = 0.70
loadDataset(r"C:\Users\Tyler\Downloads\Demographic_Statistics_By_Zip_Code.csv", split, trainingSet, testSet)
print('Train Set: ' + repr(len(trainingSet)))
print('Test Set: ' + repr(len(testSet)))

# Make prediction
predictions = []
k = 16

for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)

accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')
