# Part 5: Reusable Functions (don't repeat yourself)
from data import students

# 15.  Write a function `filter_by_track(students, track)` that returns all students in a given track. Test it with `"AI"` and `"Data"


def filter_by_track(students, track):
    new_list1 = []
    for student in students:
        if student["track"] == track:
            new_list1.append(student)
