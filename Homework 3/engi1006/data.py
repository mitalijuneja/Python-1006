####
# Mitali Juneja (mj2944)
# Homework 3B part 2 = contains functions for processing the csv file data to
# prepare it for the algorithms
####



from random import sample
def postProcessCSV(dataset):
    '''
    Takes the dataset as an N x M list of lists.

    Modifies the dataset in-place to:
        - strip the client ID
        - convert the float columns to be floats instead of strings
    '''
    for row in dataset:
        row = row.pop(0)
        for item in row:
            item = float(item)
    
   
def datasetInfo(dataset):
    '''
    Takes the dataset as an N x M list of lists.

    Returns the following statistics as a dictionary:
        rows: N from above, as an integer
        columns: M from above, as an integer
        benign: Number of benign entries in dataset
        malignant: Number of malignant entries in dataset
    '''


    ret = {}

    ret['rows'] = len(dataset)
    ret['columns'] = len(dataset[0])
    
    mal = 0
    ben = 0
    for data in dataset:
        if data[0] == 'M':
            mal += 1
        else:
            ben += 1
    
    ret['benign'] = ben
    ret['malignant'] = mal

    return ret


def splitDataset(dataset, test_percentage=20):
    '''
    Takes the dataset as an N x M list of lists.

    Returns 2 subsets of the dataset:
        the first is the testing part, which should be 
        test_percentage percent of N
        the second is the training part, which should be 
        100-test_percentage percent of N
    
    
    Randomly selects test_percentage % of the data for testing, remaining data 
    left for training
    '''
    # compute how many data entries are test_percentage % of dataset
    test_num = int(len(dataset) * test_percentage/100)
    # create a list of test_num random indices in dataset (without replacement)
    test_idx = sample(range(0, len(dataset)), test_num) 
    
    test_data = []
    training_data = []
    
    # for dataset entries with index in test_idx, add to test_data, otherwise
    #add to training_data
    for i in range(len(dataset)):
        if i in test_idx:
            test_data.append(dataset[i])
        else:
            training_data.append(dataset[i])
        
    

    return test_data, training_data