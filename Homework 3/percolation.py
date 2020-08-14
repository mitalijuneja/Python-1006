# *******************************************************
# Mitali Juneja (mj2944)
# Homework 3B part 1 = functions for creating a site vacancy matrix
# and performing percolation on it
#
#
# percolation module
# HW3 Part B
# ENGI E1006
# *******************************************************

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def read_grid(input_file):
    """Create a site vacancy matrix from a text file.

    input_file is a file object associated with the
    text file to be read. The method should return
    the corresponding site vacancy matrix represented
    as a numpy array
    """
    
    size = int(input_file.readline().strip())
    vac_mat = np.zeros((size, size))
    line_num = 0
    for line in input_file:
        vac_mat[line_num] = line.strip().split()
        line_num += 1
    
    return vac_mat
        


def write_grid(filename, sites):
    """Write a site vacancy matrix to a file.

    filename is a String that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
   
    file = open(filename, 'w')
    file.write(str(sites.shape[0]) + "\n")
    for arr in sites:
        for num in arr:
            file.write(str(int(num)) + " ")
        file.write("\n")
    
    file.close()
    
    


def percolate(mat, x, y):
    """If there is water (2) in mat[y,x] (location in mat with x coordinate
    x and y coordinate y), then percolate into spots below, left, and 
    right of mat[y,x] that are still in the bounds of mat and are 
    vacant (1)))"""
   
    if x >= 0 and x < mat.shape[0] and y >= 0 and y < mat.shape[1]:
        if int(mat[y,x]) == 2:
            if x + 1 < mat.shape[0] and int(mat[y,x + 1]) == 1:
                mat[y,x + 1] = 2
                mat = percolate(mat, x + 1, y)
            if x > 0 and int(mat[y,x - 1]) == 1:
                mat[y,x - 1] = 2
                mat = percolate(mat, x - 1, y)
            if y + 1 < mat.shape[1] and int(mat[y + 1,x]) == 1:
                mat[y + 1,x] = 2
                mat = percolate(mat, x, y + 1)
    return mat
            
           
        


def flow(sites):
    """Makes vacant sites (1) in the top row filled with water (2) and 
    then starts recursive percolate() function to fill in the rest 
    of the matrix
    
    Returns a matrix of vacant/full sites (1=vacant, 0=full)

    sites is a numpy array representing a site vacancy matrix. This
    function should return the corresponding flow matrix generated
    through vertical percolation
    """
    flow_mat = np.empty_like(sites)
    flow_mat[:] = sites
    for c in range(flow_mat.shape[1]):
        if flow_mat[0,c] == 1:
            flow_mat[0,c] = 2.0
            flow_mat = percolate(flow_mat, c, 0)
        
    return flow_mat
 

def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """
    return 2 in flow_matrix[-1]


def make_sites(n, p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy
    matrix with site vaccancy probability p
    """
    
    return (np.random.random((n, n)) > (1 - p)).astype(int)


def plot(before, after):
    """Plots the before and after matrices using matplotlib
    """
    fig, axes = plt.subplots(1, 2)

    axes[0].pcolor(before, cmap='Greys_r')
    axes[0].set_ylim(before.shape[0], 0)

    l = ListedColormap(['black', 'white', 'blue'])
    axes[1].pcolor(after, cmap=l)
    axes[1].set_ylim(before.shape[0], 0)
    plt.show()
