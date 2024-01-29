class Student:
    def __init__(self,student_id,marks,age):
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def set_student_id(self,student_id):
        self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id
    def set_marks(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_age(self,age):
        self.__age = age
    def get_age(self):
        return self.__age
    
    def validate_marks(self):
        if self.__marks >= 0 and self.__marks <= 100:
            return True
        else:
            return False
        
    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age() == True and self.validate_marks() == True:
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False

student = Student(1001,65,21)

if student.check_qualification() == True:
    print("Student Qualified")
else:
    print("Student is disqualified")


print("Age is Valid: ",student.validate_age())
print("Qualified: ",student.check_qualification())
print("Marks is Valid: ",student.validate_marks())

print(student.get_student_id())
student.set_student_id(202)
print(student.get_student_id())

print(student.get_age())
student.set_age(18)
print(student.get_age())
print("Age is Valid: ",student.validate_age())

print(student.get_marks())
student.set_marks(67)
print(student.get_marks())



