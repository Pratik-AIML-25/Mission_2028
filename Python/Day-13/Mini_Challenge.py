'''
Student Email Generator

Take input:
Full Name
Roll Number
Department

Generate an email like:
pratik.yadav23aiml@sageuniversity.in                                                                                                          '''


# CODE👇
full_name = input("Enter Full Name: ")
roll_number = input("Enter Roll Number: ")
department = input("Enter Department: ")

name_parts = full_name.lower().split()
name = ".".join(name_parts)

email = name + roll_number + department.lower() + "@sageuniversity.in"

print("Generated Email:")
print(email)


''' Output:-

    Example:
    Input: Enter Full Name: Pratik Yadav
           Enter Roll Number: 23
           Enter Department: AIML
    Output: Generated Email:
            pratik.yadav23aiml@sageuniversity.in                                                                                              '''