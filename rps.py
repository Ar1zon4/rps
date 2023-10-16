
import sys
import random
print("")

playerchoice = input("Enter ...... \n 1 for Rock \n 2 for scissors \n 3 for paper\n\n")

player= int(playerchoice)

if player < 1 or player > 3:
    sys.exit('Enter either 1,2 or 3')


computerchoice = random.choice('123')

computer = int(computerchoice)

print('')
print('Your choice' + " " + playerchoice)
print('Computer choice' + "  " + computerchoice)


if playerchoice == 1 and computerchoice == 3:
    print('You win! ;)')
elif playerchoice == 2 and computerchoice ==3:
    print('You win! ;)')
elif playerchoice == 3 and computerchoice ==1:
     print('You win! ;)')
elif playerchoice == computerchoice:
    print('Tie game! :|')
else:
    print('You Lose! :(')














# playerchoice = input("Enter....\n1 for Rock,\n2 for Paper, or \n3 for scissors:\n\n")
# # print(playerchoice)

# player = int(playerchoice)
 
# if player < 1 | player< 3:
#     sys.exit("You must enter 1,2 or 3.")


# computerchoice = random.choice("123")

# computer = int(computerchoice)

# print("")
# print("You chose"+  playerchoice +  ".")
# print("Python chose" + computerchoice + ".")
# print("")

# if player == 1 and computer == 3:
#     print("You win")
# elif player == 2 and computer == 1:
#     print("You win")    
# elif player == 3 and computer == 2:
#     print("You win")
# elif player == computer:
#     print("Tie Game!")    

# else:
#     print("Python Wins! ")  
