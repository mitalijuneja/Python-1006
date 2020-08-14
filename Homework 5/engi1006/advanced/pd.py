
#########
# Mitali Juneja (mj2944)
# Homework 5 = statistics functionality with pandas
# 
#########

import pandas as pd

def advancedStats(data, labels):
    '''Advanced stats should leverage pandas to calculate
    some relevant statistics on the data.

    data: numpy array of data
    labels: numpy array of labels
    '''
    # convert to dataframe
    df = pd.DataFrame(data)


    # print skew and kurtosis for every column
    skew = df.skew(axis = 0)
    kurt = df.kurtosis(axis = 0)
    for col in range(df.shape[1]):
        print("Column {} statistics".format(col))
        print("\tSkewness = {}\tKurtosis = {}".format(skew[col], kurt[col]))
        
    
    # assign in labels
    df["labels"] = labels

    print("\n\nDataframe statistics")

    # groupby labels into "benign" and "malignant"
    mean = df.groupby(["labels"]).mean().T
    sd = df.groupby(["labels"]).std().T
    
    

    # collect means and standard deviations for columns,
    # grouped by label
    b_mean = mean.iloc[:,0]
    m_mean = mean.iloc[:,-1]
    b_sd = sd.iloc[:,0]
    m_sd = sd.iloc[:,-1]
   

    # Print mean and stddev for Benign
    print("Benign Stats:")
    
    print("Mean")
    print(b_mean)
    print("SD")
    print(b_sd)

    print("\n")

    # Print mean and stddev for Malignant
    print("Malignant Stats:")
    
    print("Mean")
    print(m_mean)
    print("SD")
    print(m_sd)

