# Program-1 :- Create a set of 5 fruits and print it.

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
print(fruits)

''' Output:-
    {'Mango', 'Apple', 'Papaya', 'Orange', 'Banana'}                                                                                       '''


# Program-2 :- Print the length of a set.

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
print(len(fruits))

''' Output:-
    5                                                                                                                                      '''


# Program-3 :- Add one item using add().

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
fruits.add("Guava")
print(fruits)

''' Output:-
    {'Papaya', 'Apple', 'Guava', 'Orange', 'Mango', 'Banana'}                                                                               '''


# Program-4 :- Add multiple items using update().

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
fruits.update(["Guava","Pear"])
print(fruits)

''' Output:-
    {'Orange', 'Papaya', 'Guava', 'Pear', 'Apple', 'Banana', 'Mango'}                                                                       '''


# Program-5 :- Remove an item using remove().

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
fruits.remove("Banana")
print(fruits)

''' Output:-
    {'Apple', 'Papaya', 'Orange', 'Mango'}                                                                                                   '''


# Program-6 :- Remove an item using discard().

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
fruits.discard("Banana")
print(fruits)

''' Output:-
    {'Apple', 'Orange', 'Papaya', 'Mango'}                                                                                                   '''


# Program-7 :- Remove a random item using pop().

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
fruits.pop()
print(fruits)

''' Output:-
    Since sets are unordered, you don't know which item will be removed.                                                                     '''


# Program-8 :- Clear the set.

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
fruits.clear()
print(fruits)

''' Output:-
    set()                                                                                                                                    '''


# Program-9 :- Check whether "Apple" exists in the set.

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
if "Apple" in fruits:
    print("Found")

''' Output:-
    Found                                                                                                                                    ''' 


# Program-10 :- Print all items using a for loop.

# CODE👇
fruits = {"Mango","Orange","Banana","Apple","Papaya"}
for item in fruits:
    print(item)

''' Output:-
    Papaya
    Orange
    Apple
    Mango
    Banana                                                                                                                                   '''


# Program-11 :- Find the union of two sets.

# CODE👇
A = {10, 20, 30}
B = {30, 40, 50}
print(A | B)

''' Output:-
    {10, 20, 30, 40, 50}                                                                                                                     '''


# Program-12 :- Find the intersection of two sets.

# CODE👇
A = {10, 20, 30}
B = {30, 40, 50}
print(A & B)

''' Output:-
    {30}                                                                                                                                     '''


# Program-13 :- Find the difference between two sets.

# CODE👇
A = {10, 20, 30}
B = {30, 40, 50}
print(A - B)

''' Output:-
    {10, 20}                                                                                                                                  '''


# Program-14 :- Find the symmetric difference between two sets.

# CODE👇
A = {10, 20, 30}
B = {30, 40, 50}
print(A ^ B)

''' Output:-
    {40, 10, 50, 20}                                                                                                                          '''


# Program-15 :- Create a set from a list containing duplicate values and print the result.

# CODE👇
numbers = [10, 20, 30, 20, 40, 10, 50]
unique_numbers = set(numbers)
print(unique_numbers)

''' Output:-
    {40, 10, 50, 20, 30}                                                                                                                      '''