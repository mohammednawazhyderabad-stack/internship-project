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

choices = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for rock ,1 for paper or 2 for scissors: "))
if user_choice >=3 or user_choice<0:
    print("invalid choice! You loose")
else:
    print("you choose:")
    print(choices[user_choice])
    computer_choice= random.randint(0,2)
    print("computer choose:")
    print(choices[computer_choice])
    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice ==0 and computer_choice==2:
        print("You Win! rock smashes scissors!")
    elif user_choice ==2 and computer_choice==1:
        print("You Win! scissors cut Paper !")
    elif user_choice ==1 and computer_choice==0:
        print("You Win! paper covers rock!")
    else:
        print("You Loose!")
