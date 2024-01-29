class Student:
    def __init__(self,student_id,marks,age,course_id,fees):
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age
        self.__course_id = course_id
        self.__fees = fees

    def set_fees(self,fees):
        self.__fees = fees
    def get_fees(self):
        return self.__fees
    def set_course_id(self,course_id):
        self.__course_id = course_id
    def get_course_id(self):
        return self.__course_id
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
    
    def choose_course(self, course_id):
        self.__course_id = course_id
        if (course_id == 1001) or (course_id == 1002):
            self.set_course_id(course_id)
            self.set_fees(15500.0)
            if self.__marks > 85:
                self.__fees = 0.75 * self.__fees
            return True
        else:
            return False
        
student = Student(101,86,21,1001,25575.0)

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
student.set_marks(90)
print(student.get_marks())


print(student.get_course_id())
print(student.get_fees())

print(student.choose_course(1001))
print(student.get_fees())


