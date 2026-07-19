'''
Student ID Card

Take input from the user:
Name
Roll Number
Branch
Semester

Store everything in a dictionary.
Print the details in a neat format like an ID card.                                                                                          '''

# CODE👇

student = {
    "Name": input("Enter your name: "),
    "Roll Number": input("Enter your roll number: "),
    "Branch": input("Enter your branch: "),
    "Semester": input("Enter your semester: ")
}
print("\n----- STUDENT ID CARD -----")
print("Name        :", student["Name"])
print("Roll Number :", student["Roll Number"])
print("Branch      :", student["Branch"])
print("Semester    :", student["Semester"])
print("---------------------------")


''' Output:-

    Enter your name: Pratik Yadav
    Enter your roll number: 42
    Enter your branch: BTech(Hons.)CSE-AIML
    Enter your semester: 3rd

    ----- STUDENT ID CARD -----
    Name        : Pratik Yadav
    Roll Number : 42
    Branch      : BTech(Hons.)CSE-AIML
    Semester    : 3rd
    ---------------------------                                                                                                              '''