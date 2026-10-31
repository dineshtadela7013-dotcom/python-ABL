
total_classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

if total_classes <= 0 or attended < 0 or attended > total_classes:
    print("Invalid attendance details")

else:
    percentage = (attended / total_classes) * 100

    print("Current Attendance:", round(percentage, 2), "%")

    required = 75
    extra_classes = 0

    while percentage < required:

        total_classes += 1
        attended += 1
        extra_classes += 1

        percentage = (attended / total_classes) * 100

    print("Extra Classes Required:", extra_classes)
    print("Final Attendance:", round(percentage, 2), "%")
