students = {
    "Anderson": 88,
    "Martinez": 92,
    "Clark": 79,
    "Lewis": 85,
    "Walker": 90
}

total = 0

print("Student Name   Grade")
print("---------------------")

for name in students:

    print(f"{name:15} {students[name]}")
    total += students[name]

class_average = total / len(students)

print("---------------------")
print(f"Class Average: {class_average:.2f}")
