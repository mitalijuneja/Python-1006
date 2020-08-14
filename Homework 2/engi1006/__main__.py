from . import parseCSV, askConfig, datasetInfo

def main():
    # Ask user for configuration variables
    config = askConfig()

    # Read CSV
    csv = parseCSV(config["filename"])

    # Print out table information
    dataset_info = datasetInfo(csv)
    print("Dataset size: {} x {}".format(dataset_info["rows"], dataset_info["columns"]))


if __name__ == "__main__":
    main()
