# Program-1 :- Simple Function

# CODE
def hello():
    print("Hello World")

hello()


# Program-2 :- Print your Name

# CODE
def my_name(name):
    print(name)

my_name("Pratik Yadav")


# Program-3 :- Add Two Numbers

# CODE
def add():
    a = int(input("First Number : "))
    b = int(input("Second Number : "))
    print("Sum =", a + b)

add()


# Program-4 :- Function with Parameters

#CODE
def greet(name):
    print("Hello", name)

greet("Pratik")


# Program-5 :- Add Using Parameters

# CODE
def add(a, b):
    print("Sum =", a + b)

add(10, 20)


# Program-6 :- Square of Number

# CODE
def square(num):
    print("Square =", num * num)

square(5)


# Program-7 :- Cube

# CODE
def cube(num):
    print("Cube =", num ** 3)

cube(4)


# Program-8 :- Even or Odd

# CODE
def check(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check(15)


# Program-9 :- Largest Number

# CODE
def largest(a, b):
    if a > b:
        return a
    return b

largest(12, 25)


# Program-10 :- Function Returning Sum

# CODE
def add(a, b):
    return a + b

result = add(8, 9)
print(result)


# Program-11 : Return Square

# CODE
def square(num):
    return num * num

print(square(6))


# Program-12 :- Return Maximum

# CODE
def maximum(a, b):
    if a > b:
        return a
    return b

print(maximum(20, 15))


# Program-13 :- Factorial Function

# CODE
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

print(factorial(5))


# Program-14 :- Print Table

# CODE
def table(num):

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

table(7)


# Program-15 :- Greeting Function

# CODE
def welcome(name):
    print("Welcome", name)

name = input("Enter your name: ")

welcome(name)