import random
import log_rps
rock ="""
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
scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
ls =[rock,paper,scissors]
user_choice = int(input("Enter your chosie in number 0:for rock  1:for paper 2:for scissors : "))
computer_choice = random.randint(0,2)
if user_choice >=3 or user_choice < 0:
    print("You enter in valid option")
else:
    print(ls[user_choice])
    computer_choice = random.randint(0, 2)
    print(ls[computer_choice])
    if computer_choice == user_choice :
        print("""
        ██╗████████╗███████╗    ██████╗ ██████╗  █████╗ ██╗    ██╗
        ██║╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔══██╗██║    ██║
        ██║   ██║   ███████╗    ██║  ██║██████╔╝███████║██║ █╗ ██║
        ██║   ██║   ╚════██║    ██║  ██║██╔══██╗██╔══██║██║███╗██║
        ██║   ██║   ███████║    ██████╔╝██║  ██║██║  ██║╚███╔███╔╝
        ╚═╝   ╚═╝   ╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ 
                                                          """)
    elif computer_choice == 0 & user_choice == 2 :
        print("""
        ░█░█░█▀█░█░█░░░█░░░█▀█░█▀▀░█▀▀
        ░░█░░█░█░█░█░░░█░░░█░█░▀▀█░█▀▀
        ░░▀░░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀""")
    elif user_choice == 0 & computer_choice == 2 :
        print("""
        ░█░█░█▀█░█░█░░░█░█░▀█▀░█▀█
        ░░█░░█░█░█░█░░░█▄█░░█░░█░█
        ░░▀░░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀""")
    elif computer_choice > user_choice :
        print("""
        ░█░█░█▀█░█░█░░░█░░░█▀█░█▀▀░█▀▀
        ░░█░░█░█░█░█░░░█░░░█░█░▀▀█░█▀▀
        ░░▀░░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀""")
    elif user_choice > computer_choice :
        print("""
        ░█░█░█▀█░█░█░░░█░█░▀█▀░█▀█
        ░░█░░█░█░█░█░░░█▄█░░█░░█░█
        ░░▀░░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀""")


