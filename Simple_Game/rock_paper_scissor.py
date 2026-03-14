# Author :- Biresashis Das

# Here we will choose the number particular for rock, paper and scissor and the computer randomly choose one number particularly from rock, paper and scissor.
# Than both them will be compare and based on that we will get our output.
       ''' 
           Rock beats scissors
           Scissors beats paper
           Paper beats rock 
           
       '''
#Player decides an option  
import random
t = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor. '))
print("You have choosen👇")
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

if t == 0:
    print("Rock",rock)
elif t == 1:
    print("Paper",paper)
elif t == 2:
    print("Scissor",scissor)
#If user inputs an invalid option, they will be notifed
else:
    print("Invalid option. Please select the option from the given line.")
#Computer randomly decides an option
computer = random.randint(0,2)
print("Computer have choosen👇")
if t < 3:
    if computer == 0:
        print("Rock",rock)
    elif computer == 1:
        print("Paper",paper)
    elif computer == 2:
        print("Scissor",scissor)
else:
    print("Restart the Game.")
#Tie outcome
if t == 0 and computer == 0 or t == 1 and computer == 1 or t == 2 and computer == 2:
    print("Its a draw")
#Loss outcome
elif t == 0 and computer == 1 or t == 1 and computer == 2 or t == 2 and computer == 0:
    print("You loose the match")
#Win outcome
elif t == 0 and computer == 2 or t == 1 and computer == 0 or t == 2 and computer == 1:
    print("You won the match")

    
    
# Sample Output

#       What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor. 0
#       You have choosen👇
#       Rock 
#           _______
#       ---'   ____)
#             (_____)
#             (_____)
#             (____)
#       ---.__(___)

#       Computer have choosen👇
#       Paper 
#            _______
#       ---'    ____)____
#                  ______)
#                 _______)
#                _______)
#       ---.__________)

#       You loose the match
    
    
    
    
