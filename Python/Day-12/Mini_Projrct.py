'''
Username Generator

Take input:

First Name
Last Name
Birth Year

Generate a username like:

pratikyadav2006

Example:

Enter First Name: Pratik
Enter Last Name: Yadav
Enter Birth Year: 2006

Generated Username:
pratikyadav2006                                                                                                                              '''

# CODE👇
first_name = input("Enter First Name: ").strip()
last_name = input("Enter Last Name: ").strip()
birth_year = input("Enter Birth Year: ").strip()
username = first_name.lower() + last_name.lower() + birth_year
print("\nGenerated Username:")
print(username)

''' Input:- Enter First Name: Pratik
            Enter Last Name: Yadav
            Enter Birth Year: 2006
            
    Output:- Generated Username:
             pratikyadav2006                                                                                                                 
    
    Explanation:-
    lower() converts the first and last names to lowercase.
    strip() removes any extra spaces from the input.
    The '+' operator joins all the strings together to create the username.                                                                   '''