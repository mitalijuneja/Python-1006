############
# Mitali Juneja (mj2944)
# Homework 4 = Course class for engi1006_simulator
#
#
############


from statistics import mean
import matplotlib.pyplot as plt

from .student import Student
from .assignment import Assignment


class Course(object):
    def __init__(self, teacher):
        """
        constructor for Course object
        initializes instance variables (teacher, students, assignments, grades
        for all students, names of all students)
        """
        
        self.teacher = teacher
        self.students = []
        self.assignments = []
        self.grades = []
        self.names = []

    def __add__(self, other):
        """
        + for course object
        register student instances, assign assignment instances
        returns the modified self instance
        """
        
        if isinstance(other, Student):
            self.register(other)
        elif isinstance(other, Assignment):
            self.assign(other)
        return self

    def __repr__(self):
        """
        representation of Course object
        teacher, students, number of assignments, assignment difficulty,
        average grade
        """
        
        ret = '\n'
        ret += '\tProfessor: {}\n'.format(self.teacher)
        ret += '\tNumber of Students: {}\n'.format(len(self.students))

        if len(self.students):
            ret += '\t\t' + ','.join(str(s) for s in self.students) + '\n'

        ret += '\tNumber of Assignments: {}\n'.format(len(self.assignments))

        if len(self.assignments):
            ret += '\t\t' + ','.join(str(a.difficulty) for a in self.assignments) + '\n'

        if len(self.assignments) > 0:
            ret += 'Average grade: {}'.format(sum(self.grades) / len(self.grades))
        return ret
    
    def register(self, other):
        """
        how to register a student
        adds student to students
        adds student name to names
        adds placeholder grade of 0 to grades
        """
        
        self.students.append(other)
        self.names.append(other.name)
        self.grades.append(0)
        
    def assign(self, other):
        """
        how to assign an assignment
        retrieve each students grade and add it to list of grades 
        for that assignment
        update each student's average grade
        add the assignment to assignments
        """
        
        for i,student in enumerate(self.students):
            grade = Student.getGrade(student, other.difficulty)
            other.grades.append(grade)
            num_assgn = len(self.assignments)
            self.grades[i]=(num_assgn * self.grades[i] + grade)/(1 + num_assgn)
            
        self.assignments.append(other)
            

    def finish(self):
        """
        prints final details = class average, teacher pay
        """
        
        # print average of all grades
        print(f'Class Average: {mean(self.grades)}')
        self.teacher.calcPay(self.assignments, len(self.students))
        # print teacher pay
        print(f'Teacher pay: {self.teacher.pay}')
        

    def plot(self):
        """
        plotting functionality (grades for each student by assignment, grades
        for each assignment by student, difficulty of assignments)
        """
        
        fig, axes = plt.subplots(3, 1)
        axes[0].set_title('Grades by assignment')
        axes[0].set_ylabel('Grade')

        handles = []
        for s in self.students:
            # array initially empty
            handles.append(axes[0].scatter(list(range(len(self.assignments))), s.grades))

        # set legend
        axes[0].legend(handles, [s.name for s in self.students], loc='upper right', bbox_to_anchor=(1.35, 1), fancybox=True)

        # set x axis labels and ticks
        axes[0].set_xticks([i for i in range(len(self.assignments))])

        # next subplot
        axes[1].set_title('Grades by Student')
        axes[1].set_ylabel('Grade')

        handles = []
        for a in self.assignments:
            # array initially empty
            handles.append(axes[1].scatter(list(range(len(self.names))), a.grades))

        # set legend
        axes[1].legend(handles, [i for i in range(len(self.assignments))], loc='upper right', bbox_to_anchor=(1.3, 1), fancybox=True)

        # set x axis labels and ticks
        axes[1].set_xticks([i for i in range(len(self.students))])
        axes[1].set_xticklabels([s.name for s in self.students])

        # next subplot

        axes[2].set_title('Assignment Difficulty')
        axes[2].set_ylabel('Difficulty')

        difficulties = [a.difficulty for a in self.assignments]
        axes[2].plot(list(range(len(self.assignments))), difficulties)

        # set x axis labels and ticks
        axes[2].set_xticks([i for i in range(len(self.assignments))])

        # plot
        plt.subplots_adjust(right=.7, hspace=1)
        plt.show()