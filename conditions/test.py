"""
If grade is 90 or higher, print "A"
Else if grade is 80 or higher, print "B"
Else if grade is 70 or higher, print "C"
Else if grade is 60 or higher, print "D"
Else, print "F"
"""

student_grade = int(input("Enter your grade : "))

if student_grade >= 90:
    print("A")
elif student_grade >= 80:
    print("B")
elif student_grade >= 70:
    print("C")
elif student_grade >= 60:
    print("D")
else:
    print("F")