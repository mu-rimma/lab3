import parent_class


class Bachelor(parent_class.Student):
    def get_average_grade(self):
        return super().get_average_grade()


class Master(parent_class.Student):
    def get_average_grade(self):
        return super().get_average_grade() * 1.2


object_b = Bachelor('Petrov I.A.', [3, 4, 5, 4])
object_m = Master('Sidorov A.O.', [3, 4, 5, 4])

for student in (object_b,object_m):
    ag = student.get_average_grade()
    print(f"{student.get_private_attr()}, {student.grades}, {ag}\n")