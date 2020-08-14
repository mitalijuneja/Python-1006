#############
# Mitali Juneja (mj2944)
# Homework 4 = utility functions for engi1006_simulator
#
#
#############


from random import random

def skillToGrade(skill, difficulty):
    """
    calculate student grade based on student skill and assignment difficulty
    return grade
    """
    
    hardness_mult = (random() > (difficulty / 100 - skill / 100)) * 2 - 1
    skill_mult = (random() < (skill / 100 - difficulty / 100)) * 2 - 1

    hard = random()*difficulty/10
    study = random()*skill/10

    return (skill / 100 * 40) + 50 + (hardness_mult * hard) + (skill_mult * study)


def printOpener():
    """
    opener for engi1006_simulator
    """
    
    print('Hello! Welcome to the ENGI1006 class modeler.\n'
          'With this program we will simulate the ENGI1006 course at '
          'Columbia University')


def getTeacherName():
    """
    store teacher name from user input
    """
    
    return input("First, what would you like to name the Professor: ")