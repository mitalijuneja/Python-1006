Mitali Juneja (mj2944)
Homework 3 part B

1. completed functions in percolation.py
completed flow() and percolate() in the following way = 

for flow(), filled in any open (1) spots in the top row with water (2) and then called percolate() on those spots only

for percolate(), if the location passed in has water (2), then call percolate() on spots that are open (1) below, to the left, to the right if they are in the bounds of the matrix

2. completed the functions in data.py
for splitDataset(), selected test_percentage % of the data for testing randomly without replacement