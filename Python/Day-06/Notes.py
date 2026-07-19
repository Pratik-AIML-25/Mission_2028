'''
TOPIC :- Loops

✨ What is a Loop?
A loop repeats a block of code multiple times.

Instead of writing:

CODE👇

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

You write👇

for i in range(5):
    print("Hello")


✨ Types of Loops
Python is mainly of two loops.

1. for loop
Used when you know how many times to repeat.

CODE👇

for i in range(5):
    print(i)

Output

0
1
2
3
4


2. while loop
Used when you don't know how many times.

CODE👇

count = 1

while count <= 5:
    print(count)
    count += 1

Output

1
2
3
4
5


3. range()
Most important function.

Example-1

CODE👇

for i in range(5):
    print(i)

Ootput

0
1
2
3
4

Example-2

CODE👇

for i in range(1,6):
    print(i)

Output

1
2
3
4
5

Example-3

for i in range(1,11,2):
    print(i)

Output

1
3
5
7
9

Syntax

range(start, stop, step)

'''