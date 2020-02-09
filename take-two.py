import random

rules="""
Winning Rules of the Rock paper scissor game as follows:
Rock vs paper->paper wins
Rock vs scissor->Rock wins
paper vs scissor->scissor wins
"""

choices="""
Enter choice:
1. Rock
2. paper
3. scissor
"""

elements=["rock","paper","scissors"]

print(rules)
# input() fails for strings in repl.it
# play_again="yes"
# while play_again in ["y","Y","yes","Yes"]:
play_again=1
while play_again == 1:
    print(choices)

    user_choice = int(input("Your turn: "))
    while user_choice > 3 or user_choice < 1: 
      user_choice = int(input("Give a valid choice: ")) 

    user_choice -= 1 # convert to arrary index
    print("user choice is: %s" % elements[user_choice]) 
    print("\nNow its computer turn.......") 

    comp_choice = random.randint(0, 2)
    while comp_choice == user_choice: 
      comp_choice = random.randint(0, 2)

    print("Computer choice is: %s " % elements[comp_choice]) 
    print("%s vs %s" % (elements[user_choice],elements[comp_choice]))

    # paper & rock
    if((user_choice == 0 and comp_choice == 1) or
       (user_choice == 1 and comp_choice == 0 )): 
        print("paper wins => ") 
        result = elements[1] # "paper"
    # scissors & rock
    elif((user_choice == 0 and comp_choice == 2) or
         (user_choice == 2 and comp_choice == 0)): 
        print("Rock wins =>") 
        result = elements[0] # "rock"
    # scissors & paper?
    else: 
        print("scissor wins =>") 
        result = elements[2] # "scissors"
    # what about the draw?

    if result == elements[user_choice]: 
        print("<== User wins ==>") 
    else: 
        print("<== Computer wins ==>") 
          
    print("Do you want to play again?") 
    play_again = int(input("1 for yes; 2 for no: "))

