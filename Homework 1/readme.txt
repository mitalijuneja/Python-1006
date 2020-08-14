Mitali Juneja (mj2944)
Homework 1 part B

1. hw1b_problem1.py
contains the 3 functions (get_name_length() returns the length of the name, is_even() returns true if the name has an even length false otherwise, print_letters() prints each letter in the name in its own line). main() uses these functions to produce an output similar to sample output in the assignment

2. lists.py
implements all of the list functions described in the assignment

lists_a = swaps first and last elements
lists_b = shifts all elements down by 1 by making a new list and determining the new indices for the elements in the shifted list
lists_c = replaces all even elements with 0
lists_d = makes a new list, copies over the first and last elements, then replaces the middle elements with the maximum of its 2 neighbors
lists_e = removes the middle (odd length) or middle 2 (even length) elements of the list
lists_f = creates a list of all even elements and a list of all odd elements. Then returns the concatenation of the 2
lists_g = returns the second largest element in the list. If there are less than 2 elements, returns None (no 2nd largest possible). Otherwise, traverses the list and keeps track of the largest 2 elements that have appeared so far. Once the entire list is traversed, returns the smaller element in the list that contains the 2 largest elements seen. However, if that element is equal to the largest one in the list, return None since this would occur if the list had all identical elements.
lists_h = checks adjacent elements to see if any adjacent elements are in decreasing order (return -1). otherwise, if entire list is traversed return 1 (must be increasing)
lists_i = checks adjacent elements to see if they are duplicates (returns 1). otherwise, if entire list is traversed return -1 (no duplicates)
lists_j = creates a list that stores unique elements as the list is traversed. if an item in the list is already in the unique elements list, then it is a duplicate (return 1). otherwise, if entire list is traversed return -1 (no duplicates)
