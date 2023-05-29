import random
l = ["ROCK","PAPER","SCISSOR"]

print("-"*40)
print('''
ROCK PAPER AND SCISSORS
''')
print("-"*40)
print('''
Game rule is that you will play these game for 10 rounds 
''')
while True:
    user_count = 0
    computer_count = 0

    name = input("Enter your name --> ")
    print("*"*40)
    print("WELCOME ",name)
    print("*"*40)

    print("*"*40)
    user = int(input('''
    press 1 to play the Game
    press 2 to Exit the Game   ---> '''))
    print("*"*40)
   
    if user == 1:
        for i in range (1,11):
            user_input = int(input('''
            1 ROCK
            2 PAPER
            3 SCISSOR
            '''))
            if user_input == 1:
                user_choice = "ROCK"
            elif user_input == 2:
                user_choice = "PAPER"
            elif user_input == 3:
                user_choice = "SCISSOR"
            else:
                print("invalid number")
            computer_choice = random.choice(l)
            if computer_choice == user_choice:
                print("Computer value",computer_choice)
                print("user value" ,user_choice)
                print("GAME DRAW")
                user_count = user_count + 1
                computer_count = computer_count + 1
            elif (user_choice == "PAPER" and computer_choice == "ROCK") or (user_choice == "ROCK" and computer_choice == "SCISSOR") or (user_choice == "SCISSOR" and computer_choice == "PAPER"):
                print("user value",user_choice)
                print("computer value",computer_choice)
                print("YOU WIN")
                user_count = user_count + 1
            else:
                print("user value",user_choice)
                print("computer value",computer_choice)
                print("COMPUTER WIN")
                computer_count = computer_count + 1
    
        if user_count == computer_count:
            print("GAME HAS BEEN DRAW")
            print("User Score",user_count)
            print("Computer Score",computer_count)
        elif user_count > computer_count :
            print("YOU WIN THESE MATCH")
            print("User Score",user_count)
            print("Computer Score",computer_count)
        else:
            print("COMPUTER HAS WIN THESE MATCH")
            print("User Score",user_count)
            print("Computer Score",computer_count)

        repeat = input("Do you want to play the Game agai ..?(yes/no) --> ")
        if repeat == "no":
            print(" See you soon ")
            break
    else:
        break
