class Student:
    def __init__(self, name, grades):
        self.__name = name
        self.grades = grades

    def get_private_attr(self):
        return self.__name

    def get_average_grade(self):
        print('Parent method')
        return sum(self.grades) / len(self.grades)
