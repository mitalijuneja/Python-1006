#!/usr/bin/env python3
# -*- coding: utf-8 -*-
####
# @ author Mitali Juneja (mj2944)
#
# Homework 1b Problem 1 = contains functions for name length, even and odd,
# and printing individual letters. main() uses these functions to display 
# output similar to sample output in assignment
#
####


def get_name_length(name):
    """ returns the length of the name"""

    return len(name)


def is_even(name):
    """ returns true if the name has an even length, false otherwise"""
    
    return get_name_length(name) % 2 == 0


def print_letters(name):
    """ prints each letter in the name separately in its own line"""
    
    for i in range(get_name_length(name)):
        print("Letter %d is = %c" % (i, name[i]))
    

def main():
    """ combines the above 3 functions to produce output similar to sample 
        output in assignment"""
        
    name = input("What is your name? ")
    print ("Hello %s" % (name))

    print ("You have %d letters in your name" % (get_name_length(name)))
    
    if (is_even(name)):
        print("You have an even number of letters in your name")
    else:
        print ("You have an odd number of letters in your name")

    print_letters(name)

if __name__ == "__main__":
    main()


