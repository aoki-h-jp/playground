"""
16. Write a Python program to find the second lowest grade of any student(s) from the given names and
grades of each student using lists and lambda. Input number of students, names and grades of each student.
Input number of students: 5
Name: S ROY
Grade: 1
Name: B BOSE
Grade: 3
Name: N KAR
Grade: 2
Name: C DUTTA
Grade: 1
Name: G GHOSH
Grade: 1
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR
"""
STUDENTS = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]


if __name__ == '__main__':
    STUDENTS.sort(key=lambda x: x[1])
    second_grade = sorted(set([datum[1] for datum in STUDENTS]))[-2]
    print(f'Second lowest grade: {second_grade}')
    second_grade_students = [datum for datum in STUDENTS if datum[1] == second_grade]
    print('Names:')
    for datum in second_grade_students:
        print(f'{datum[0]}')
