students = [
    {"name": "Ahmed", "grades": [85, 90, 78]},
    {"name": "Sara", "grades": [92, 88, 95]},
    {"name": "Omar", "grades": [76, 84, 80]}
]

print("Student Averages:")
for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{name}: Average Grade = {average:.2f}")