# Program-1 :- Create a string and print it.

# CODE👇
name = "Pratik Yadav"
print(name)

''' Output:-
    Pratik Yadav                                                                                                                             '''


# Program-2 :- Print the length of a string.

# CODE👇
name = "Pratik Yadav"
print(len(name))

''' Output:-
    12                                                                                                                                        '''


# Program-3 :- Print the first and last character.

# CODE👇
name = "Pratik Yadav"
print(name[0],name[-1])

''' Output:-
    P v                                                                                                                                      '''


# Program-4 :- Convert a string to uppercase.

# CODE👇
name = "Pratik Yadav"
print(name.upper())

''' Output:-
    PRATIK YADAV                                                                                                                              '''


# Program-5 :- Convert a string to lowercase.

# CODE👇
name = "Pratik Yadav"
print(name.lower())

''' Output:-
    pratik yadav                                                                                                                              '''


# Program-6 :- Count how many times a character appears.

# CODE👇
name = "Pratik Yadav"
print(name.count("a"))

''' Output:- 
    3                                                                                                                                         '''


# Program-7 :- Replace one word with another.

# CODE👇
name = "Pratik Yadav"
new_name = name.replace("Yadav","Coder")
print(new_name)

''' Output:-
    Pratik Coder                                                                                                                              '''


# Program-8 :- Reverse a string using slicing.

# CODE👇
name = "Pratik Yadav"
reverse_name = name[::-1]
print(reverse_name)

''' Output:-
    vadaY kitarP                                                                                                                             
    
    name[::-1] returns the string in reverse order using slicing.                                                                             '''


# Program-9 :- Check whether a string starts with a particular letter.

# CODE👇
name = "Pratik Yadav"
if name.startswith("P"):
    print("The string starts with 'P'.")
else:
    print("The string does not start with 'P'.")

''' Output:-
    The string starts with 'P'.                                                                                                               '''


# Program-10 :- Check whether a string ends with a particular letter.

# CODE👇
name = "Pratik Yadav"
if name.endswith("v"):
    print("The string ends with 'v'.")
else:
    print("The string does not end with 'v'.")

''' Output:-
    The string ends with 'v'.                                                                                                               '''


# Program-11 :- Take user input and print it in title case.

# CODE👇
name = input("Enter a string: ")
print(name.title())

''' Example:-
    Input:- Enter a string: pratik yadav
    Output:-Pratik Yadav                                                                                                                      
    
    The title() method converts the first letter of each word to uppercase and the remaining letters to lowercase.                            '''


# Program-12 :- Check whether the entered string is a digit.

# CODE👇
message = input("Enter a string: ")
if message.isdigit():
    print("The entered string is a digit.")
else:
    print("The entered string is not a digit.")

''' Example-1 :-
    Input :- Enter a string: 12345
    Output :- The entered string is a digit.
    
    Example-2 :-
    Input :- Enter a string: Pratik123
    Output :- The entered string is not a digit.
    
    isdigit() returns True if all characters in the string are digits (0–9); otherwise, it returns False.                                    '''


# Program-13 :- Print every character using a for loop.

# CODE👇
name = "Pratik Yadav"
for ch in name:
    print(ch)

''' Output:-
    P
    r
    a
    t
    i
    k
 
    Y
    a
    d
    a
    v                                                                                                                                         '''


# Program-14 :- Find the index of a character using find().

# CODE👇
name = "Pratik Yadav"
index = name.find("d")
print(index)

''' Output:-
    9                                                                                                                                         '''


''' Program-15 :- Take a full name and print:
                  
                  First Name:
                  Last Name:
                  Total Characters:                                                                                                           '''

# CODE👇
full_name = input("Enter your full name: ").strip()
name_parts = full_name.split()
print("First Name:", name_parts[0])
print("Last Name:", name_parts[-1])
print("Total Characters:", len(full_name.replace(" ", "")))

''' Example:-
    Input:- Enter your full name: Pratik Yadav
    Output:- First Name: Pratik
             Last Name: Yadav
             Total Characters: 13      
    
                                                                                                                                                                                                                          
    split() separates the full name into words.
    name_parts[0] gives the first name.
    name_parts[-1] gives the last name.
    len(full_name.replace(" ", "")) counts the characters excluding spaces. If you want to include spaces in the count, use len(full_name) 
    instead.                                                                                                                                  '''


