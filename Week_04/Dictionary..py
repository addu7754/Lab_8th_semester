#Create a dictionary of student names and marks
student_details = {
    'Aman': 85,
    'joey': 60,
    'Chandler': 92,
    'monica': 75,
    'Gulzar': 88,
    'Ammar': 70
}

#Display students scoring above 75
print("Students scoring above 75:")
for name, marks in student_details.items():
    if marks > 75:
        print(f"{name}")
