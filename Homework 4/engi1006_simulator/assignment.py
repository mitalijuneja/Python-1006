##############
# Mitali Juneja (mj2944)
# Homework 4 = Assignment class for engi1006_simulator
#
#
##############



class Assignment(object):
    def __init__(self, difficulty):
        """
        constructor for Assignment object
        initializes instance variables (difficulty of assignment (0 - 100), 
        grades of each student on this assignment))
        """
        
        self.difficulty = difficulty
        self.grades = []

    def __repr__(self):
        """
        representation of Assignment object
        difficulty and number of students
        """
        
        return "\tAssignment Difficulty: {}\n\tStudent Count:{}".format(self.difficulty, len(self.grades))
