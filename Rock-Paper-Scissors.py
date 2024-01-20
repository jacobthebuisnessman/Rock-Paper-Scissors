import random
print("""
1 - rock
2 - paper
3 - scissors""")
###################################
def rand():
    bot = random.randrange(1,4)
    if bot == 1:
        print("Bot Plays Rock")
    elif bot == 2:
        print("Bot Plays Paper")
    else:
        print("Bot Plays Scissors")
###################################
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
###################################
user = int(input("input: "))
a = 1
while a < 50:
    print("\n")
    a = a + 1
if user == 1:
    print("You Play Rock")
elif user == 2:
    print("You Play Paper")
else:
    print("You Play Scissors")
###################################
rand()

