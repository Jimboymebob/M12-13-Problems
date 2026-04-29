last_names = [
    "Anderson",
    "Martinez",
    "Clark",
    "Lewis",
    "Walker",
    "Hall",
    "Allen",
    "Young",
    "King",
    "Wright"
]

exam_scores = [88, 92, 79, 85, 90, 76, 95, 84, 87, 91]

def display_students(names, scores):

    print("Students and Scores")
    print("-------------------")

    for i in range(len(names)):
        print(f"{names[i]:10} {scores[i]}")

def display_reverse(names, scores):

    print("\nStudents and Scores in Reverse")
    print("------------------------------")

    for i in range(len(names) - 1, -1, -1):
        print(f"{names[i]:10} {scores[i]}")

display_students(last_names, exam_scores)
display_reverse(last_names, exam_scores)
