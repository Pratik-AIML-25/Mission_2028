'''
TOPIC :- Sets in Python

✨ What is a Set?
A Set is a collection of unique and unordered elements.

1)Duplicate values are automatically removed.
2)Sets do not support indexing.
3)Sets are mutable (you can add or remove elements).

Example:
fruits = {"Apple", "Banana", "Mango"}
print(fruits)

✨ Creating a Set

numbers = {10, 20, 30, 40}
print(numbers)

An empty set is created using:

empty_set = set()

Don't use {} because it creates an empty dictionary.

✨ Duplicate Values

numbers = {10, 20, 10, 30, 20}
print(numbers)

Output:
{10, 20, 30}

Python automatically removes duplicates.

✨ add()
Adds a single element.

fruits = {"Apple", "Banana"}
fruits.add("Mango")
print(fruits)

✨ update()
Adds multiple elements.

fruits = {"Apple", "Banana"}
fruits.update(["Mango", "Orange"])
print(fruits)

✨ remove()
Removes an element.

fruits.remove("Apple")

If the element does not exist, Python gives an error.

✨ discard()

fruits.discard("Apple")

No error is generated if the element doesn't exist.

✨ pop()
Removes a random element.

fruits.pop()

Since sets are unordered, you don't know which item will be removed.

✨ clear()

Deletes all elements.

fruits.clear()
print(fruits)

Output:
set()

✨ len()
Returns the number of elements.

print(len(fruits))

✨ Membership Operator
if "Apple" in fruits:
    print("Found")

✨ Union
Combines two sets.

A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))

Output:
{1, 2, 3, 4, 5}

Or:

print(A | B)

✨ Intersection

Returns common elements.

print(A.intersection(B))

Output:
{3}

Or:

print(A & B)

✨ Difference
Returns elements present in the first set but not in the second.

print(A.difference(B))

Output:
{1, 2}

Or:

print(A - B)

✨ Symmetric Difference
Returns uncommon elements from both sets.

print(A.symmetric_difference(B))

Output:
{1, 2, 4, 5}

Or:

print(A ^ B)

✨ Looping Through a Set

fruits = {"Apple", "Banana", "Mango"}
for item in fruits:
    print(item)

✨ Important Points

Feature	                        Set

Ordered	                        No
Indexing	                    No
Duplicates Allowed	            No
Mutable	                        Yes
Unique Values	                Yes

✨Methods You Must Remember

add()
update()
remove()
discard()
pop()
clear()
len()
union()
intersection()
difference()
symmetric_difference()

'''