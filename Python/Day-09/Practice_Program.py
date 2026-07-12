# Program-1 :- Create a tuple of 5 fruits and print it.

# CODE👇
fruits = ("Apple", "Banana", "Mango", "Orange", "Papaya")
print(fruits)


# Program-2 :- Print first element.

# CODE👇
numbers = (10,20,30,40,50)
print(numbers[0])


# Program-3 :- Print last element.

# CODE👇
numbers = (10,20,30,40,50)
print(numbers[-1])


# Program-4 :- Print tuple length.

# CODE👇
numbers = (10,20,30,40,50)
print(len(numbers))


# Program-5 :- Print second element.

# CODE👇
numbers = (10,20,30,40,50)
print(numbers[1])


# Program-6 :- Print first three elements.

# CODE👇
numbers = (10,20,30,40,50)
print(numbers[:3])


# Program-7 :- Check if Apple exists.

# CODE👇
fruits = ("Apple", "Banana", "Mango", "Orange", "Papaya")
if "Apple" in fruits:
    print("Found")


# Program-8 :- Count occurrence of 10.

# CODE👇
numbers = (10,20,10,30,10)
print(numbers.count(10))


# Program-9 :- Find index of 30.

# CODE👇
numbers = (10,20,30,40)
print(numbers.index(30))


# Program-10 :- Print all items using loop.

# CODE👇
fruits = ("Apple", "Banana", "Mango", "Orange", "Papaya")
for item in fruits:
    print(item)


# Program-11 :- Tuple Packing.

# CODE👇
name = input("Enter Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
student = (name, age, city)
print(student)



# Program-12 :- Tuple Unpacking.

# CODE👇
name = input("Enter Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
student = (name, age, city)
name, age, city = student
print("Name :", name)
print("Age  :", age)
print("City :", city)


# Program-13 :- Maximum value.

# CODE👇
numbers = (10,25,8,50,80)
print(max(numbers))


# Program-14 :- Minimum value.

# CODE👇
numbers = (10,25,8,50,80)
print(min(numbers))


# Program-15 :- Sum of tuple.

# CODE👇
numbers = (10,25,8,50,80)
print(sum(numbers))