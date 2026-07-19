# Program-1 :- Print numbers from 1 to 10.

# CODE👇
for i in range(1,11):
    print(i)


# Program-2 :- Print numbers from 10 to 1.

# CODE👇
for i in range(10, 0, -1):
    print(i)


# Program-3 :- Print your name 5 times.

# CODE👇
name = input("Enter your name: ")

for i in range(5):
    print(name)


# Program-4 :- Print even numbers from 1 to 20.

# CODE👇
for i in range(2, 21, 2):
    print(i)


# Program-5 :- Print odd numbers from 1 to 20.

# CODE👇
for i in range(1, 21, 2):
    print(i)


''' Program-5 :- Print multiplication table of any number.

                Example
                Enter number: 7

                Output
                7 x 1 = 7
                7 x 2 = 14
                ...
                7 x 10 = 70                                                                                                                 '''

# CODE👇
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


''' Program-7 :- Find sum from 1 to N.

                Example
                Enter N = 5
                Output - 15                                                                                                                 '''

# CODE👇
n = int(input("Enter N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)


''' Program-8 :- Find factorial.

                Example
                5! = 120                                                                                                                   '''

# CODE👇
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)


# Program-9 :- Count from 1 to 100.

# CODE👇
for i in range(1, 101):
    print(i)


''' Program-10 :- Print squares from 1 to 10.

                    Output

                    1
                    4
                    9
                    16
                    ...
                    100                                                                                                                     '''


# CODE👇
for i in range(1, 11):
    print(i * i)


# Program-11 :- Print cubes from 1 to 10.

# CODE👇
for i in range(1, 11):
    print(i ** 3)


''' Program-12 :- Count total digits.

                  Example
                  Input = 12
                  Output = 5                                                                                                                  '''

# CODE👇
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count = count + 1

print("Total digits =", count)


''' Program-13 :- Reverse a number.

                  Example
                  Input = 1234
                  Output = 4321                                                                                                                      '''

# CODE👇
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)


''' Program-14 :- Check palindrome number.

                  Example
                  Input = 121
                  Output = Palindrome                                                                                                               '''

# CODE👇
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


''' Program-15 :- Find sum of digits.
                  Example
                  Input = 1234
                  Output = 10                                                                                                              '''

# CODE👇
num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits =", sum)
