'''
TOPIC :- Tuples

✨ A tuple is like a list, but once created, it cannot be changed (immutable).
✨ A tuple is an ordered collection.
✨ Tuples are IMMUTABLE (cannot be changed).

✨ Creating Tuple
fruits = ("Apple", "Banana", "Mango")
print(fruits)

✨ Single element tuple
a = (10,)
print(a)

✨ Accessing Elements
print(fruits[0])
print(fruits[-1])

✨ Slicing
print(fruits[0:2])

✨ Length
print(len(fruits))

✨ Count
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

✨ Index
print(numbers.index(20))

✨ Membership
print("Apple" in fruits)

✨ Loop
for item in fruits:
    print(item)

✨ Packing
student = ("Pratik", 20, "Bhopal")

✨ Unpacking
name, age, city = student

print(name)
print(age)
print(city)

'''