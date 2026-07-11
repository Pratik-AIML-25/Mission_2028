# Program-1 :- Create a list of 5 fruits and print it.

# CODE👇
fruits = ["Apple","Mango","Banana","Orange","Papaya"]
print("Fruits List:",fruits)


# Program-2 :- Print the first element.

# CODE👇
numbers = [10, 20, 30, 40, 50]
print("First element is:", numbers[0])


# Program-3 :- Print the last element.

# CODE👇
numbers = [10, 20, 30, 40, 50]
print("Last element is:", numbers[-1])


# Program-4 :- Replace second element with another value.

# CODE👇
numbers = [10, 20, 30, 40, 50]
numbers[1] = 70
print("Updated List:", numbers)


# Program-5 :- Find length of list.

# CODE👇
numbers = [10, 20, 30, 40, 50]
print("Length of the list:", len(numbers))


# Program-6 :- Add one item using append().

# CODE👇
fruits = ["Apple","Mango","Banana","Orange","Papaya"]
fruits.append("Guava")
print("Fruits List:",fruits)


# Program-7 :- Insert one item at index 2.

# CODE👇
fruits = ["Apple","Mango","Banana","Orange","Papaya"]
fruits.insert(2, "Kiwi")
print("Updated List:", fruits)


# Program-8 :- Remove one item.

# CODE👇
fruits = ["Apple","Mango","Banana","Orange","Papaya"]
fruits.remove("Banana")
print("Updated List:", fruits)


# Program-9 :- Delete last item using pop().

# CODE👇
fruits = ["Apple","Mango","Banana","Orange","Papaya"]
fruits.pop()
print("Updated List:", fruits)


# Program-10 :- Print all items using for loop.

# CODE👇
fruits = ["Apple","Mango","Banana","Orange","Papaya"]
for fruit in fruits:
    print(fruit)


# Program-11 :- Check if "Apple" exists.

# CODE👇
fruits = ["Apple","Mango","Banana","Orange","Papaya"]
if "Apple" in fruits:
    print("Found")


# Program-12 :- Create list of 5 numbers and print their sum.

# CODE👇
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print("Sum of the numbers:", total)


# Program-13 :- Print largest number from list.

# CODE👇
numbers = [10, 25, 4, 50, 80]
largest = max(numbers)
print("Largest number:", largest)


# Program-14 :- Print smallest number from list.

# CODE👇
numbers = [10, 25, 4, 50, 80]
smallest = min(numbers)
print("Smallest number:", smallest)


''' Program-15 :- 
Print each item with its index using enumerate().

Example:
fruits = ["Apple","Banana","Mango"]
Output : 0 Apple
         1 Banana
         2 Mango                                                                                                                         '''

# CODE👇
fruits = ["Apple","Banana","Mango"]
for index, item in enumerate(fruits):
    print(index, item)
