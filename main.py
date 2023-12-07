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
map=[rock,paper,scissors]
print("Welcome to the rock paper game")
choice1 = int(
    input('''Please enter your choice\n1=>rock\n2=>paper\n3=>scissors\n'''))
print(map[choice1-1])
comp_choice=random.choice(map)
print("Computer choice is:\n",comp_choice)
if choice1==1 and comp_choice==scissors:
	print("You Win")
elif choice1==1 and comp_choice==paper:
	print("You Win")
elif choice1==1 and comp_choice==rock:
	print("Match Draw")
elif choice1==2 and comp_choice==rock:
	print("You Win")
elif choice1==2 and comp_choice==paper:
	print("Match Draw")
elif choice1==3 and comp_choice==paper:
	print("You Win")
elif choice1==3 and comp_choice==scissors:
	print("Match Draw")
else:
	print("You Lose")