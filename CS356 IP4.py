# CS356 Big Data Analytics: Tyler Koenig

import csv
import random
import math
import operator

with open(r"C:\Users\Tyler\Documents\CTU\CS356\KickstarterDataset\ks-projects-201801.csv", encoding="utf-8") as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))

# Ignore invalid characters
bytes.decode(csvfile, encoding="utf-8", errors="ignore")


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
loadDataset(r"C:\Users\Tyler\Documents\CTU\CS356\KickstarterDataset\ks-projects-201801.csv", split, trainingSet, testSet)
print('Train Set: ' + repr(len(trainingSet)))
print('Test Set: ' + repr(len(testSet)))

# Make prediction
predictions = []
k = 569

for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)

accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')
