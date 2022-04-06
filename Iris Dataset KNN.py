import csv
import random
import math
import operator

with open(r"C:\Users\Tyler\Downloads\archive\Iris.csv") as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))


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


# Test loadDataset function
trainingSet = []
testSet = []
loadDataset(r"C:\Users\Tyler\Downloads\archive\Iris.csv", 0.7, trainingSet, testSet)
print('Load Dataset Function Test: ')
print('Train: ' + repr(len(trainingSet)))
print('Test: ' + repr(len(testSet)))


# Calculate Euclidean Distance
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# Test euclideanDistance function
data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclideanDistance(data1, data2, 3)
print('Euclidean Distance Function Test: ')
print(repr(distance))


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


# Test getNeighbors function
trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
testInstance = [5, 5, 5]
k = 1
neighbors = getNeighbors(trainSet, testInstance, 1)
print('Neighbors Function Test: ')
print(neighbors)


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


# Test getNeighbors function
neighbors = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
response = getResponse(neighbors)
print('Response Function Test: ')
print(response)


# Calculate accuracy of predictions
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] is predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


# Test getAccuracy function
testSet = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print('Accuracy Function Test: ')
print(accuracy)


# Prepare data
print('Results: ')
trainingSet = []
testSet = []
split = 0.70
loadDataset(r"C:\Users\Tyler\Downloads\archive\Iris.csv", split, trainingSet, testSet)
print('Train Set: ' + repr(len(trainingSet)))
print('Test Set: ' + repr(len(testSet)))

# Make prediction
predictions = []
k = 3

for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)
    print('> predicted-' + repr(result) + ', actual-' + repr(testSet[x][-1]))

accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')

