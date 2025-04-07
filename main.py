import random

while True:
  print("Welcome to the number guessing game!")
  input("(press enter to continue)")
  print(
      "I will think of a number between 1 and 100. Your goal is to guess it in as few attempts as possible."
  )
  print(
      "After each guess, I will tell you if your guess is too high, too low, or correct along with the amount of attempts it took."
  )
  print("Choose a difficulty.")
  print("1. Easy")
  print("2. Medium")
  print("3. Hard")

  difficulty = input("Type a number: ")

  while difficulty not in ["1", "2", "3"]:
    difficulty = input("Invalid input. Type a number: ")
  attempts = 0

  if difficulty == "1":
    attempts = 10
    print("Easy mode selected. Good luck!")
    input("(press enter to continue)")
  elif difficulty == "2":
    attempts = 7
    print("Medium mode selected. Good luck!")
    input("(press enter to continue)")
  else:
    attempts = 4
    print("Hard mode selected. Good luck!")
    input("(press enter to continue)")

  correctNumber = random.randint(1, 100)
  print("I have thought of a number between 1 and 100.")
  print("You have", attempts, "attempts to guess it.")

  tries = attempts

  while tries > 0:
    guess = input("Type in your guess: ")
    if not guess.isdigit():
      print("Invalid input. Please type in a number.")
      continue
    guess = int(guess)
    if guess < 1 or guess > 100:
      print("Invalid input. Please type in a number between 1 and 100.")
      continue
    if guess != correctNumber:
      tries -= 1
      if guess < correctNumber:
        print("The correct number is higher than ", guess)
      else:
        print("The correct number is lower than ", guess)
      print("You have", tries, "attempts left.")
    else:
      print("Congratulations! You guessed the correct number in",
            attempts - tries, "attempt(s).")
      break
    if tries == 0:
      print("The correct number was ", correctNumber)
  print("Would you like to play again?")
  print("1. Yes")
  print("2. No")
  playAgain = input("Type a number: ")

  while playAgain not in ["1", "2"]:
    playAgain = input("Invalid input. Type a number: ")
  if playAgain == "2":
    print("Thank you for playing!")
    break
  if playAgain == "1":
    print("Let's play again!")
    input("(press enter to continue)")
