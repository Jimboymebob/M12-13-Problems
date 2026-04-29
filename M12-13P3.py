last_names = []
scores = []


file = open("students.txt", "r")

for line in file:

    data = line.strip().split()

    last_names.append(data[0])
    scores.append(int(data[1]))

file.close()

def display_students(names, scores):

    print("Students and Scores")
    print("-------------------")

    for i in range(len(names)):
        print(f"{names[i]:10} {scores[i]}")

def highest_score(names, scores):

    high_var = 0
    high_index = 0

    for i in range(len(scores)):

        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i

    print("\nHighest Score")
    print(f"{names[high_index]} {high_var}")

def lowest_score(names, scores):

    low_var = 999
    low_index = 0

    for i in range(len(scores)):

        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print("\nLowest Score")
    print(f"{names[low_index]} {low_var}")

display_students(last_names, scores)
highest_score(last_names, scores)
lowest_score(last_names, scores)
