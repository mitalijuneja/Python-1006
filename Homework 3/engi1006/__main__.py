from . import parseCSV, askConfig, datasetInfo, postProcessCSV, splitDataset

def main():
    # Ask user for configuration variables
    config = askConfig()

    # Print out configuration parameters
    print("Reading filename: {}".format(config["filename"]))

    # Read CSV
    csv = parseCSV(config["filename"])

    # Do some post processing on the csv
    postProcessCSV(csv)

    # Print out table information
    dataset_info = datasetInfo(csv)

    print("Dataset size: {} x {}".format(dataset_info["rows"], dataset_info["columns"]))
    print("Number of benign: {}".format(dataset_info["benign"]))
    print("Number of malignant: {}".format(dataset_info["malignant"]))

    input("\n\nHit enter to run algorithm\n\n")

    print("Splitting dataset into {}% for training and {}% for testing".format(100 - config["testpercentage"], config["testpercentage"]))
    test, train = splitDataset(csv, config["testpercentage"])

    print("Test dataset has {} entries".format(len(test)))
    print("Train dataset has {} entries".format(len(train)))



if __name__ == "__main__":
    main()
