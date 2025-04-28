class Teacher: # parent class
    def __init__(self, teacherName, teacherAge, teacherClass, teacherProfession):
        self.teacher_name = teacherName
        self.teacher_age = teacherAge
        self.teacher_class = teacherClass
        self.teacher_profession = teacherProfession
    

    def details(self):
        print(f'The details for the user are: \n{self.teacher_name} \n{self.teacher_age} \n{self.teacher_class} \n{self.teacher_profession}')

    def __str__(self):
        return('This class needs the following arguments:\nteacherName\nteacherAge\nteacherClass\nteacherProfession ')
    

teacher1  = Teacher('Mr. Luseno', 53, 'Form2Meridian', "Chemist Teacher")
print("Teacher details details")
print(teacher1)
teacher1.details()

print('\n\n')
# inheritance === child/derived class
class Student(Teacher):
    def __str__(self):
        return 'This Student class and inherits from Teacher Class'

student1 = Student('Tony Stalk', 40, 'Form 2 Y', "Student")
print("Student details")
student1.details()