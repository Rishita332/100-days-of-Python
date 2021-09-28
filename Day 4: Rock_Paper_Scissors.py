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
import random
user_choice=int(input("What's your choice? Type 0 for rock, 1 for paper and 2 for scissors\n"))
d={0: rock, 1:paper, 2: scissors}
if user_choice>2 or user_choice<0:
    print("Invalid choice!!!!")
else:
    print("User's choice is ",d[user_choice])

computer_choice=random.choice(d)
print("Computer's Choice is ", computer_choice)

if user_choice==0:
    if computer_choice==d[1]:
        print("You Lose!!")
    elif computer_choice==d[2]:
        print("You Win!!!") 
    else:
        print("You tied!")  
if user_choice==1:
    if computer_choice==d[2]:
        print("You Lose!!")
    elif computer_choice==d[0]:
        print("You Win!!!") 
    else:
        print("You tied!")   
if user_choice==2:
    if computer_choice==d[0]:
        print("You Lose!!")
    elif computer_choice==d[1]:
        print("You Win!!!") 
    else:
        print("You tied!")                 
