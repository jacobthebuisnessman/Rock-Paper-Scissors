import random
print("""
1 - rock
2 - paper
3 - scissors""")

def rand():
    a = random.randrange(1,3)
    print(a)
    if x == 3 and a == 2:
        print("user wins")
    elif x == 2 and a == 3:
        print("user wins")
    elif x == 1 and a == 1:
        print("user wins")
    else:
        print("machine wins")

x = int(input("input: "))
rand()

