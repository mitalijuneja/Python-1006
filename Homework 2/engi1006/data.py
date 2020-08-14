####
# Mitali Juneja (mj2944)
# Homework 2b Problem 2 = contains functions for the csv data
####

def datasetInfo(dataset):
    '''
    Takes the dataset as an N x M list of lists.

    Returns the following statistics as a dictionary:
        rows: N from above, as an integer
        columns: M from above, as an integer
    '''
    # return a dictionary
    ret = {}
    # Implement your code here
    ret["rows"] = len(dataset)
    ret["columns"] = len(dataset[0])

    return ret