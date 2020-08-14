###########
# Mitali Juneja (mj2944)
# Homework 4 = Person class for engi1006_simulator
#
#
###########

class Person(object):
    def __init__(self, name):
        """
        constructor for Person object
        initializes instance variable (name)
        """
        
        self.name = name

    def __repr__(self):
        """representation of Person object
        name
        """
        
        return self.name
