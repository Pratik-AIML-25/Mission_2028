''' 
Topic: User Input (input()) + Type Casting

1. Taking input()

CODE

    name = input("Enter your name: ")
    print("Hello", name)
    
Output 
    
    Enter your name: Pratik
    Hello Pratik
    
👉 input() hamesha string return karta hai.


2. Taking Age

CODE

    age = input("Enter your age: ")
    print("Your age is", age)

Output

    Enter your age: 19
    Your age is 19

Ye abhi bhi string hai.


3. Type Casting
✨Convert string → integer

CODE

    age = int(input("Enter your age: "))
    print(age)

✨Convert to float

CODE

    height = float(input("Enter height: "))
    print(height)

✨Convert to string

CODE

    num = 50
    print(str(num))


4. Addition

CODE

    a = int(input("First Number: "))
    b = int(input("Second Number: "))

print("Sum =", a + b)

Example

    First Number: 10
    Second Number: 20

    Sum = 30


5. Subtraction    

CODE

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print("Difference =", a - b)


6. Multiplication

CODE

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print("Product =", a * b)


7. Division

CODE

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print("Division =", a / b)

8. Square of Number

CODE

    num = int(input("Enter Number: "))
    print("Square =", num * num)


9. Area of Rectangle

CODE

    length = float(input("Length: "))
    breadth = float(input("Breadth: "))

    print("Area =", length * breadth)


10. Swap Two Numbers (Using Third Variable)

CODE

    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    temp = a
    a = b
    b = temp

    print("A =", a)
    print("B =", b)
'''