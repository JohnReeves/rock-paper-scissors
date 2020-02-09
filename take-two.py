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
play_again="yes"

print(rules)

hello=input("what is your name? ")
print(hello)

while play_again in ["y","Y","yes","Yes"]:
    print(choices)

    user_choice = int(input("Your turn: "))
    while user_choice > 3 or user_choice < 1: 
      user_choice = int(input("Give a valid choice: ")) 

    print("user choice is: %s" % elements[user_choice]) 
    print("\nNow its computer turn.......") 

    comp_choice = random.randint(1, 3) -1
    while comp_choice == user_choice: 
      comp_choice = random.randint(1, 3) -1

    print("Computer choice is: %s " % elements[comp_choice]) 

    print("%s vs %s" % (elements[user_choice],elements[comp_choice]))

    if((user_choice == 1 and comp_choice == 2) or
       (user_choice == 2 and comp_choice ==1 )): 
        # print("paper wins => ", end = "") 
        print("paper wins => ") 
        result = elements[1] # "paper"
    elif((user_choice == 1 and comp_choice == 3) or
         (user_choice == 3 and comp_choice == 1)): 
        # print("Rock wins =>", end = "") 
        print("Rock wins =>") 
        result = elements[0] # "rock"
    else: 
        # print("scissor wins =>", end = "") 
        print("scissor wins =>") 
        result = elements[2] # "scissors"

    if result == elements[user_choice]: 
        print("<== User wins ==>") 
    else: 
        print("<== Computer wins ==>") 
          
    # print("Do you want to play again? (Y/N)") 
    play_again = input("Do you want to play again? (Y/N) ")
  

