
####
# @author Mitali Juneja (mj2944)
#
# Homework 1b Problem 2 = contains the lists functions that each produce an
# output according to the assignment description
#
####


def lists_a(lst):
    """ Swaps the first and last elements of the list"""
    
    if len(lst):
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


def lists_b(lst):
    """ Shifts all elements by one to the right and move the last element 
        into the first position"""
        
    shifted_list = [0]*len(lst)
    for i in range(len(lst)):
        new_idx = (i + 1) % len(lst)
        shifted_list[new_idx] = lst[i]
    return shifted_list


def lists_c(lst):
    """ Replaces all even elements with 0"""
    
    for i in range(len(lst)):
        if (lst[i] % 2 == 0):
            lst[i] = 0
    return lst


def lists_d(lst):
    """ Replaces each element except the first and last by the larger of 
        its two neighbors"""
    
    new_list = [0] * len(lst)
    for i in range (len(lst)):
        if i == 0 or i == len(lst) - 1:
            new_list[i] = lst[i]
        else:
            new_list[i] = max(lst[i - 1], lst[i + 1])
    return new_list


def lists_e(lst):
    """ Removes the middle element if the list length is odd, or the 
        middle two elements if the length is even"""
    if len(lst) == 0:
        return lst
    mid = len(lst) // 2
    if (len(lst) % 2 == 0):
        del(lst[mid])
        del(lst[mid - 1])
    else:
        del(lst[mid])
        
    return lst


def lists_f(lst):
    """ Moves all even elements to the front, otherwise preserving 
        the order of the elements"""
        
    even_els = []
    odd_els = []
    for item in lst:
        if item % 2 == 0:
            even_els.append(item)
        else:
            odd_els.append(item)
    return even_els + odd_els


def lists_g(lst):
    """ Returns the second-largest element in the list"""
    # if the list has less than 2 elements, there is no 2nd largest (None)
    if len(lst) < 2:
        return None;
    
    # traverse the list and keep track of the 2 largest elements that have
    # been seen in the list at any given time
    largest_els = []
    largest_els.append(lst[0])
    largest_els.append(lst[1])
    for i in range(2, len(lst)):
        smaller_el = min(largest_els[0], largest_els[1])
        if lst[i] > smaller_el:
            largest_els.remove(smaller_el)
            largest_els.append(lst[i])
    
   # the 2nd largest element is the smaller of the 2 largest elements that
   # have been seen in the list
   # however, if that element is equal to the maximum in the list (would occur
   # if the list had all identical elements), then there is no maximum = None
    if min(largest_els[0], largest_els[1]) == max(lst):
        return None
    return min(largest_els[0], largest_els[1]) 
    
    


def lists_h(lst):
    """ Returns 1 if the list is currently sorted in increasing order, 
        else -1"""
        
    for i in range(len(lst) - 1):
        if (lst[i] > lst[i + 1]):
            return -1
    return 1


def lists_i(lst):
    """ Returns 1 if the list contains two adjacent duplicate elements, 
        else -1"""
    for i in range(len(lst) - 1):
        if (lst[i] == lst[i + 1]):
            return 1
    return -1


def lists_j(lst):
    """ Returns 1 if the list contains duplicate elements (need not be 
        adjacent), else -1"""
    
    # keep track of the unique elements in the list, if an item in the list
    # already appears in the unique_el list, then it is a duplicate
    unique_el = []
    for i in range(len(lst)):
        if (lst[i] in unique_el):
            return 1
        else:
            unique_el.append(lst[i])
    return -1
