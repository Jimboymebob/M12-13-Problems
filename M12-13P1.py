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

def display_names(names):
    print("Names in Order:")
    
    for i in range(len(names)):
        print(names[i])

def display_reverse(names):
    print("\nNames in Reverse Order:")
    
    for i in range(len(names) - 1, -1, -1):
        print(names[i])

display_names(last_names)
display_reverse(last_names)
