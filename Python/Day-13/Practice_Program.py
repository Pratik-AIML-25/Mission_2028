# Program-1 :- Take a string as input and count the number of vowels.

# CODE👇
text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Number of vowels:", count)

''' Output:-

    Example:
    Input:- Enter a string: Pratik Yadav
    Output:- Number of vowels: 5                                                                                                             '''


# Program-2 :- Take a string and count the number of consonants.

# CODE👇
text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1
print("Number of consonants:", count)

''' Output:-

    Example:
    Input:- Enter a string: Pratik Yadav
    Output:- Number of consonants: 8                                                                                                          '''


''' Program-3 :- Check whether a string is a palindrome.

                 Example:
                 Input: madam
                 Output: Palindrome                                                                                                           '''

# CODE👇
text = input("Enter a string: ").lower()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

''' Output:-

    Example: 
    Input:- Enter a string: madam
    Output:- Palindrome                                                                                                                       '''


''' Program-4 :- Reverse each word in a sentence.

                 Example:
                 Input: I Love Python
                 Output: I evoL nohtyP                                                                                                        '''

# CODE👇 
text = input("Enter a sentence: ")
words = text.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)
print(result)

''' Output:-

    Example:
    Input:- Enter a sentence: I Love Python
    Output:- I evoL nohtyP                                                                                                                    '''


''' Program-5 :- Print the initials of a full name.

                 Example:
                 Input: Pratik Yadav
                 Output: PY                                                                                                                   '''

# CODE👇 
name = input("Enter your full name: ")
words = name.split()
initials = ""
for word in words:
    initials += word[0].upper()
print(initials)

''' Output:- 
    
    Example:
    Input:- Enter your full name: Pratik Yadav
    Output:- PY                                                                                                                               '''


# Program-6 :- Remove all spaces from a string.

# CODE👇
text = input("Enter a string: ")
result = text.replace(" ", "")
print("String without spaces:", result)

''' Output:-

    Example:
    Input:- Pratik Yadav
    Output:- PratikYadav                                                                                                                      '''


''' Program-7 :- Replace every space with _.

                 Example:
                 Input: Hello World
                 Output: Hello_World                                                                                                          '''

# CODE👇
text = input("Enter a string: ")
result = text.replace(" ", "_")
print(result)

''' Output:-

    Example:
    Input: Hello World
    Output: Hello_World                                                                                                                       '''


''' Program-8 :- Print the ASCII value of every character.

                 Example:
                 Input: ABC
                 Output:
                 A = 65
                 B = 66
                 C = 67                                                                                                                       '''

# CODE👇
text = input("Enter a string: ")
for ch in text:
    print(ch, "=", ord(ch))

''' Output:-

    Example:
    Input: ABC
    Output:
    A = 65
    B = 66
    C = 67                                                                                                                                    '''


# Program-9 :- Find the longest word in a sentence.

# CODE👇
text = input("Enter a sentence: ")
words = text.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)

''' Output:-
    
    Example:
    Input:- Enter a sentence: I Love Python Programming
    Output: Longest word: Programming                                                                                                         '''


# Program-10 :- Find the shortest word in a sentence.

# CODE👇 
text = input("Enter a sentence: ")
words = text.split()
shortest_word = min(words, key=len)
print("Shortest word:", shortest_word)

''' Output:-
    
    Example:
    Input:- Enter a sentence: I Love Python Programming
    Output:- Shortest word: I                                                                                                                 '''


# Program-11 :- Count the total number of words.

# CODE👇
text = input("Enter a sentence: ")
words = text.split()
count = len(words)
print("Total number of words:", count)

''' Output:-
 
    Example:
    Input:- Enter a sentence: I Love Python Programming
    Output:- Total number of words: 4                                                                                                         '''


''' Program-12 :- Print only digits from a string.

                  Example:
                  Input: abc123xyz45
                  Output: 12345                                                                                                               '''

# CODE👇
text = input("Enter a string: ")
digits = ""
for ch in text:
    if ch.isdigit():
        digits += ch
print(digits)

''' Output:-

    Example:
    Input:- abc123xyz45
    Output:- 12345                                                                                                                            '''


# Program-13 :- Count uppercase and lowercase letters.

# CODE👇
text = input("Enter a string: ")
uppercase = 0
lowercase = 0
for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)

''' Ouput:-
  
    Example:
    Input:- Enter a string: PrAtIk YAdAv
    Output:- Uppercase letters: 6
             Lowercase letters: 5                                                                                                             '''


''' Program-14 :- Toggle the case without using swapcase().

                  Example:
                  Input: PyThOn
                  Output: pYtHoN                                                                                                              '''

# CODE👇
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print(result)

''' Output:-

    Input:- Enter a string: PyThOn
    Output:- pYtHoN                                                                                                                           '''


''' Program-15 :- Check whether two strings are anagrams.

                  Example:
                  Input:
                  listen
                  silent

                  Output:
                  Anagram                                                                                                                     '''

# CODE👇
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")

''' Output:-

    Example:
    Input:- Enter the first string: listen
            Enter the second string: silent
             
    Output:- Anagram                                                                                                                          '''