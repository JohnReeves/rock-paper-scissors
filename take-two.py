
import random

rules="""
Winning Rules of the Rock paper scissor game as follows:
Rock vs paper->paper wins
Rock vs scissor->Rock wins
paper vs scissor->scissor wins
"""

choices="""
"Enter choice:
1. Rock
2. paper
3. scissor
"""

elements=["rock","paper","scissors"]

print(rules)

while True: 
    print(choices) 
    user_choice = int(input("Your turn: ")) 
    while user_choice > 3 or user_choice < 1: 
      user_choice = int(input("Give a valid choice: ")) 

    print("user choice is: " + elements[user_choice]) 
    print("\nNow its computer turn.......") 

    comp_choice = random.randint(1, 3) 

    while comp_choice == choice: 
      comp_choice = random.randint(1, 3) 


    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("Computer choice is: " + comp_choice_name) 
  
    print(choice_name + " V/s " + comp_choice_name) 
  
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        # print("paper wins => ", end = "") 
        print("paper wins => ") 
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        # print("Rock wins =>", end = "") 
        print("Rock wins =>") 
        result = "Rock"
    else: 
        # print("scissor wins =>", end = "") 
        print("scissor wins =>") 
        result = "scissor"
  
    
    if result == choice_name: 
        print("<== User wins ==>") 
    else: 
        print("<== Computer wins ==>") 
          
    # print("Do you want to play again? (Y/N)") 
    again = input("Do you want to play again? (Y/N) ")
  
  
    
    if again == "n" or again == "N": 
      break
    else:
      pass
      

