'''
Student Marks Manager

Take marks of 5 subjects in a list.

Example:
English
Maths
Science
Computer
Physics

Output
Marks = [90,85,95,88,92]
Total = ?
Percentage = ?
Highest Marks = ?
Lowest Marks = ?

Use:
append()
sum()
max()
min()
len()                                                                                                                                     '''


# CODE👇
# Student Marks Manager

marks = []

print("Enter marks of 5 subjects:")

for i in range(5):
    mark = int(input(f"Subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nMarks =", marks)
print("Total =", total)
print("Percentage =", percentage)
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)