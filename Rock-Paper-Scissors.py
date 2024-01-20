import random
print("""
1 - rock
2 - paper
3 - scissors""")

def rand():
    bot = random.randrange(1,4)
    if bot == 1:
        print("rock")
    elif bot == 2:
        print("paper")
    else:
        print("scissors")
    
    if bot == user:
        print("draw")
    elif user == 1 and bot == 3:
        print("User Wins")
    elif user == 2 and bot == 1:
        print("User Wins")
    elif user == 3 and bot == 2:
        print("User Wins")
    else:
        print("Bot Wins")

user = int(input("input: "))
rand()

