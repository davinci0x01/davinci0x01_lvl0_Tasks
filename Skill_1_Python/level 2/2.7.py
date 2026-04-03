from random import randint

guess_num = randint(1, 25)
chances = 5

while chances != 0:
  user_input = int(input("Guess a number between 1 and 25: "))

  if user_input < guess_num:
    print("Too low")
  elif user_input > guess_num:
    print("Too high")
  else:
    print("Correct")
    print("The number is", guess_num)
    break

  chances -= 1

  if chances == 0:
    print("You lose")
    print("The number is", guess_num)
