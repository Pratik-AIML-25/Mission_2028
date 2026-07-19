'''Create a Movie Ticket Eligibility System.

Take input:

Name
Age

Conditions:

Age < 5 → Free Ticket
Age 5-17 → Child Ticket
Age 18-59 → Adult Ticket
Age 60+ → Senior Citizen Discount

Output example:

Hello Pratik
Category : Adult Ticket                                                                                            '''


# CODE👇
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello", name)

if age < 5:
    print("Category : Free Ticket")
elif age <= 17:
    print("Category : Child Ticket")
elif age <= 59:
    print("Category : Adult Ticket")
else:
    print("Category : Senior Citizen Discount")