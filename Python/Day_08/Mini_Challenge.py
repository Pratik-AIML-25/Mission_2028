'''
Shopping Cart

Take 5 product names from the user using a loop and store them in a list.

Output:
Your Shopping Cart
1. Milk
2. Bread
3. Rice
4. Sugar
5. Tea                                                                                                                                     '''


# CODE👇
cart = []

print("Enter 5 product names:")

for i in range(5):
    product = input(f"Product {i+1}: ")
    cart.append(product)

print("\nYour Shopping Cart")

for i, item in enumerate(cart, start=1):
    print(f"{i}. {item}")