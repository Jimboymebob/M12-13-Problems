students = {
    "Anderson": [88, 90, 85],
    "Martinez": [92, 94, 91],
    "Clark": [79, 81, 78],
    "Lewis": [85, 87, 84],
    "Walker": [90, 89, 93]
}

def student_averages(student_dict):

    averages = []

    for name in student_dict:

        grades = student_dict[name]

        total = 0

        for grade in grades:
            total += grade

        average = total / len(grades)

        averages.append([name, average])

    return averages

average_list = student_averages(students)

print("Student Name   Average")
print("----------------------")

for item in average_list:
    print(f"{item[0]:15} {item[1]:.2f}")

grade1_total = 0
grade2_total = 0
grade3_total = 0

for name in students:

    grade1_total += students[name][0]
    grade2_total += students[name][1]
    grade3_total += students[name][2]

count = len(students)

print("\nClass Averages")
print("----------------------")

print(f"Grade 1 Average: {grade1_total / count:.2f}")
print(f"Grade 2 Average: {grade2_total / count:.2f}")
print(f"Grade 3 Average: {grade3_total / count:.2f}")
