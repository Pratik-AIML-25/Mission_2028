'''
   Create a Number Guessing Game.

   Secret Number = 7

   User enters number.

   If correct
   Correct Guess

   Otherwise
   Wrong Guess

   Use:
   input()
   if
   for or while                                                                                                                            '''


# CODE👇
secret = 7

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct Guess")
        break
    else:
        print("Wrong Guess")
