'''
Unique Subjects

Take 5 subject names from the user.
Store them in a set.

If the user enters duplicate subjects,
they should automatically be removed.

Output:

Unique Subjects:
Python
Maths
AI
Physics
English                                                                                                                                       '''

# CODE👇

# Creating an empty set
subjects = set()

# Taking 5 subject names as input
for i in range(5):
    subject = input(f"Enter subject {i + 1}: ")
    subjects.add(subject)

# Displaying unique subjects
print("\nUnique Subjects:")
for subject in sorted(subjects):
    print(subject)


''' Output
    Enter subject 1: Python 
    Enter subject 2: Maths
    Enter subject 3: AI
    Enter subject 4: Physics
    Enter subject 5: English

    Unique Subjects:
    AI
    English
    Maths
    Physics
    Python                                                                                                                                    '''