##############
# Mitali Juneja (mj2944)
# Homework 4 = Teacher class for engi1006_simulator
#
#
##############


from .person import Person


class Teacher(Person):
    def __init__(self, name):
        """
        constructor for Teacher object
        initializes instance variables using Person constructor,
        sets pay to 0)
        """
        
        super(Teacher, self).__init__(name)
        self.pay = 0
        
    def calcPay(self, assignments, num_students):
        """
        calculate pay of teacher = sum of number of students * difficulty of
        each assignment
        """
        
        pay = 0
        for assignment in assignments:
            pay += num_students * assignment.difficulty
        self.pay = pay
  