####
# Mitali Juneja (mj2944)
# Homework 3B part 2 = contains utility functions for processing csv file
####


def parseCSV(filename):
    '''
    Read the file called "filename", expected to be a csv file.

    Return the data as a list-of-lists
    '''
    # return a list of lists
    ret = []

    with open(filename, 'r') as fp:
        for line in fp:
            ret.append(line.strip().split(','))
    return ret

def askConfig():
    '''
    Ask the user for the following config variables:
        filename: the name of the csv file
        testpercentage: percentage of dataset to reserve for testing

    Returns the information as a dictionary
    '''
    # return a dictionary
    ret = {}

    # collect variables
    ret["filename"] = input('Please provide a filename:')
    ret["testpercentage"] = int(input("What percentage of the dataset would you like to put aside for testing?"))

    return ret