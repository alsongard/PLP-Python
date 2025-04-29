import pandas as pd

students_dict = {
    'name': ["Earth", "Mars", "Jupiter", "Uranus", "Saturn"],
    'admission': ['BCS-030', 'BPS-031', 'BBM-032', 'BHR-033', 'BPY-034'],
    'grade': ['A', 'A', 'A', 'A', 'A'],
    'course': ['computer science', 'Physicist', 'BioMedical and Bioengineering', "BibleMan", "Physcology"]
}

print(len(students_dict['name']))
print(len(students_dict['admission']))
print(len(students_dict['grade']))
print(len(students_dict['course']))


student_df  = pd.DataFrame(students_dict)
print(student_df)


# extract
student_df['admision_numeric'] = student_df['admission'].str.extract(r"-(\d+)").astype(int)

print(student_df)