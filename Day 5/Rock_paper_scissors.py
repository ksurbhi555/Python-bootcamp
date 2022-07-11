import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the game")

your_choice=int(input("Press 0 for rock,1 for paper, 2 for scissors."))
if your_choice==0:
  print(f"You choose: Rock {rock}")
elif your_choice==1:
 print(f"You choose: Paper {paper}")
elif your_choice==2:
 print(f"You choose: Scissors {scissors}")

  
random_choice=random.randint(0,2)
if random_choice==0:
 print(f"Compute choose:Rock {rock}")
elif random_choice==1:
  print(f"Compute choose: Paper {paper}")
else:
  print(f"Compute choose:Scissors {scissors}")

if random_choice==your_choice:
  print("Draw")
elif random_choice==0 and your_choice==1:
 print("you wins.")
  
elif random_choice==0 and your_choice==2:
 print("computer wins.")
  
elif random_choice==1 and your_choice==2:
 print("you wins.")
  
elif random_choice==1 and your_choice==0:
 print("computer wins.")
  
elif random_choice==2 and your_choice==0:
 print("you wins.")
  
elif random_choice==2 and your_choice==1:
 print("Computer wins.")
