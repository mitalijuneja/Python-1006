
############
# Mitali Juneja (mj2944)
# Homework 5 = KNN model functionality
#
############


import numpy as np
from math import sqrt
from statistics import mode


def NNClassifier(training, testing, training_labels, testing_labels, k):
    '''Runs the Nearest Neighbor classifier:

    Args:
        training: the subset of data corresponding to the training data as a numpy matrix
        testing:  the subset of data corresponding to the testing data as a numpy matrix
        training_labels: the labels for the training data as a numpy array
        testing_labels: the labels for the testing data as a numpy array
        k: the number of nearest neighbors to use

    This function should do the following:

    - preallocate an array `labels` for the predicted labels of the testing data
    - for each row in the testing data, use knn to predict the label
    - at the end, return what percentagle of labels matched, i.e. how many labels in `labels` matched the label in `testing_labels`
    '''
    correct = 0
    # preallocate labels
    labels = np.empty_like(testing_labels)
    # for each point
        # run knn on each point and assign its label into labels
    for i in range(len(testing)):
        labels[i] = knn(training, training_labels, testing[i], k)
        if labels[i] == testing_labels[i]:
            correct += 1
    # return % where prediction matched actual

    accuracy = correct/len(testing_labels)
    return accuracy


def knn(data, data_labels, vector, k):
    '''knn should calculate the nearest neighbor

    data: the numpy array of training data
    data_labels: the numpy array of labels for the training data
    vector: a row from the testing data to calculate nearest neighbors
    k: how many nearest neighbors to find


    This function should find the `k` nearest rows in `data` relative to
    `vector`, and take a vote amongst their labels. Whichever has more (b or m), return
    that value'''
    # preallocate distance array
    distances = np.zeros(len(data_labels))
    # for each point in data
        # calculate the distance to vector, store in distance array
    for i in range(len(distances)):
        distances[i] = sqrt(((data[i].astype(float) - vector.astype(float)) ** 2).sum())
    # sort distances, and get indexes to use in data_labels (look at np.argsort)
    indexes = np.argsort(distances)
    # take vote amongs top labels
    to_vote = data_labels[indexes]
    if k % 2 == 0:
        k += 1
    return mode(to_vote[:k])
