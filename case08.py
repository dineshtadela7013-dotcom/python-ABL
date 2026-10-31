
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):

    row = []

    print("\nStudent", i + 1)

    for j in range(subjects):

        mark = int(input("Enter marks: "))
        row.append(mark)

    marks.append(row)

print("\nSTUDENT MARKS MATRIX")

for row in marks:
    print(row)

print("\nSTUDENT TOTALS")

for i in range(students):

    total = sum(marks[i])
    average = total / subjects

    print("Student", i + 1)
    print("Total:", total)
    print("Average:", round(average, 2))

print("\nSUBJECT AVERAGES")

for j in range(subjects):

    total = 0

    for i in range(students):
        total += marks[i][j]

    average = total / students

    print("Subject", j + 1, "Average:", round(average, 2))

    if average < 40:
        print("Low Performance Subject")
