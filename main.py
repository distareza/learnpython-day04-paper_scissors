import random
import my_hand_signal

#Write your code below this line 👇
selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

#input validation
if selection >= 3 or selection < 0:
  print("not in selection")
  exit(1)

print()
my_hand_signal.draw(selection)
print()

print("Computer chose:")
computer_selection = random.randint(0,2)
print()
my_hand_signal.draw(computer_selection)
print()

if selection == computer_selection:
  print("Draw")
else:
  status = "Win"
  if selection == 0 and computer_selection == 1 :
    status = "Lose"
  elif selection == 1 and computer_selection == 2 :
    status = "Lose"
  elif selection == 2 and computer_selection == 0 :  
    status = "Lose"
  print(f"You {status}")
  
