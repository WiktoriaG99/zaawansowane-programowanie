class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        leng = len(self.marks)
        sum = 0
        for mark in self.marks:
            sum = sum + mark
        avg = sum / leng
        if avg > 50:
            return True
        else:
            return False


student1 = Student("Stefan", [100, 50, 66])
print(student1.is_passed())
student2 = Student("Karolina", [10, 20, 60])
print(student2.is_passed())
