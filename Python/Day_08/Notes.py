'''
TOPIC :- Python Lists

✨ 1. What is a List?
List ek collection hai jisme multiple values store hoti hain.

CODE:-
fruits = ["Apple", "Banana", "Mango"]


✨ 2. List can store different data types.

CODE:-
data = ["Pratik", 20, 65.5, True]


✨ 3. Indexing

# CODE:-
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

# Output:-
Apple
Banana
Mango


✨ 4. Negative Indexing

# CODE:-
print(fruits[-1])
print(fruits[-2])

# Output:-
Mango
Banana


✨ 5. Change List Item

# CODE:-
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

# Output:-
['Apple', 'Orange', 'Mango']


✨ 6. List Length

# CODE:-
numbers = [10,20,30,40]

print(len(numbers))

# Output:-
4


✨ 7. Append()
Adds item at end.

# CODE:-
numbers = [10,20,30]

numbers.append(40)

print(numbers)


✨ 8. Insert()

# CODE:-
numbers = [10,30]

numbers.insert(1,20)

print(numbers)


✨ 9. Remove()

# CODE:-
numbers = [10,20,30]

numbers.remove(20)

print(numbers)


✨ 10. Pop()

# CODE
numbers = [10,20,30]

numbers.pop()

print(numbers)


✨ 11. Loop through List

# CODE:-
fruits = ["Apple","Banana","Mango"]

for fruit in fruits:
    print(fruit)


✨ 12. Check Item

# CODE:-
fruits = ["Apple","Banana"]

if "Apple" in fruits:
    print("Found")

'''