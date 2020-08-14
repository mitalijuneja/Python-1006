####
# Mitali Juneja (mj2944)
# Homework 2b Problem 2 = contains utility functions for processing csv file
###

def parseCSV(filename):
    '''
    Read the file called "filename", expected to be a csv file.

    Return the data as a list-of-lists
    '''
    # return a list of lists
    ret = []

    # Implement your code here
    file = open(filename, 'r')
    for line in file:
        line.strip()
        ret.append(line.split(','))
    file.close()
    return ret


def askConfig():
    '''
    Ask the user for the following config variables:
        filename: the name of the csv file

    Returns the information as a dictionary
    '''

    # return a dictionary
    ret = {}

    # Implement your code here
    file_name = input("Enter name of csv file = ")

    ret["filename"] = file_name
    return ret