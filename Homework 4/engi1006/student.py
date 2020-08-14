############
# Mitali Juneja (mj2944)
# Homework 4 = Student class for engi1006_simulator
#
#
############


from .person import Person
from .utilities import skillToGrade


class Student(Person):
    def __init__(self, name, skill):
        """
        constructor for Student object
        initialize instance variables using Person constructor, grades list, 
        skill level
        """
        
        super(Student, self).__init__(name)
        self.grades = []
        self.skill = skill
        
    def getGrade(self, difficulty):
        """
        get student's grade using utility function skillToGrade
        add student grade to grades list
        return grade
        """
        
        grade = skillToGrade(self.skill, difficulty)
        self.grades.append(grade)
        return grade
