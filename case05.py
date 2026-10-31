
subjects = ["Python", "Maths", "Physics"]

exam1 = []
exam2 = []

for subject in subjects:

    print("\nEnter marks for", subject)

    m1 = int(input("First Exam Marks: "))
    m2 = int(input("Second Exam Marks: "))

    exam1.append(m1)
    exam2.append(m2)

print("\nSTUDENT PERFORMANCE REPORT")

for i in range(len(subjects)):

    difference = exam2[i] - exam1[i]

    print("\nSubject:", subjects[i])
    print("First Exam:", exam1[i])
    print("Second Exam:", exam2[i])

    if difference > 0:
        print("Improvement:", difference)

    elif difference < 0:
        print("Decline:", abs(difference))

    else:
        print("No Change")

    if exam2[i] < 35:
        print("Weak Subject")

average = sum(exam2) / len(subjects)

print("\nOverall Average:", round(average, 2))
