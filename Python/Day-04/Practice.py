''' ✨Arithmetic '''

# Program-1 :- Add two numbers

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("Sum =", total)


# Program-2 :- Subtract two numbers

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
difference = num1 - num2
print("Difference =", difference)

# Program-3 :- Multiply two numbers

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
product = num1 * num2
print("Product =", product)


# Program-4 :- Divide Two Numbers

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
quotient = num1 / num2
print("Quotient =", quotient)


# Program-5 :- Find remainder

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
remainder = num1 % num2
print("Remainder =", remainder)


# Program-6 :- Square of a number

# CODE👇
num = int(input("Enter a number: "))
square = num * num
print("Square =", square)


# Program-7 :- Cube of a number

# CODE👇
num = int(input("Enter a number: "))
cube = num * num * num
print("Cube =", cube)


# Program-8 :- Power (a ** b)

# CODE👇
a = int(input("Enter the base number: "))
b = int(input("Enter the exponent: "))
power = a ** b
print("Power =", power)


''' ✨Comparison '''

# Program-9 :- Check if first number is greater than second

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 > num2
print("Result =", result)


# Program-10 :- Check if two numbers are equal

# CODE👇
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 == num2
print("Result =", result)


''' ✨Logical '''

# Program-11 :- Check voting eligibility (age >= 18)

# CODE👇
age = int(input("Enter your age: "))
result = age >= 18
print("Eligible for Voting =", result)


# Program-12 :- Check even or odd using %

# CODE👇
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


''' ✨Membership '''

# Program-13 :- Check if a letter exists in a name

# CODE👇
name = input("Enter your name: ")
letter = input("Enter a letter: ")
result = letter in name
print("Result =", result)


''' ✨Assignment '''

# Program-14 :- Demonstrate +=, -=, *=

# CODE👇
num = int(input("Enter a number: "))
num += 5
print("After += 5:", num)
num -= 3
print("After -= 3:", num)
num *= 2
print("After *= 2:", num)


''' ✨Identity '''

# Program-15 :- Compare two variables using is and is not

# CODE👇
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b =", a is b)
print("a is c =", a is c)
print("a is not c =", a is not c)