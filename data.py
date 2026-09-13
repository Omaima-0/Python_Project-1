# Assignment1- Create a system that analyzes students who enrolled in an AI bootcamp

# Dataset:
students = [
    {"name": "Lara",  "age": 23, "track": "AI",
        "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar",  "age": 31, "track": "Data",
        "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim",   "age": 27, "track": "AI",
        "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web",
        "hours_studied": 8,  "scores": [50, 65, 40]},
    {"name": "Nour",  "age": 25, "track": "AI",
        "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami",  "age": 35, "track": "Data",
        "hours_studied": 48, "scores": [88, 91, 79]},
]

# Part 1: Exploring the Data (accessing nested structures)

# 1. print the name of the first student:
print(students[0]["name"])

# 2. print Rim's scores:
print(f"this is Rim's scores: {students[2]['scores']}")

# 3. Loop through all students and print one line per student: `Lara is 23 years old and studies AI

for student in students:
    print(
        f"{student["name"]} is {student["age"]} years old and studies {student["track"]}")


# Part 2: Filtering (the most common data operation)

new_list = []
for student in students:
    if student["track"] == "AI":
        new_list.append(student)
print(new_list)

print("---------------------------------------------------")
# 5. list compehension:
new_list = [student for student in students if student["track"] == "AI"]
print(new_list)


print("---------------------------------------------------")
# 6. build a list of names based on hours_studied:
list_of_names = []
for student in students:
    if student["hours_studied"] > 30:
        list_of_names.append(student["name"])
print(list_of_names)

print("---------------------------------------------------")

new_list = [student for student in students if student["track"]
            == "AI" and student["age"] > 24]
print(new_list)
