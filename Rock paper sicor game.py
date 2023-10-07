import random
name= input("Enter your name: ")
print("0-ROCK\n1-PAPER\n2-SCISSORS")
c=u=0
while True:
    a = int(input("Enter your choice: "))
    lsts=['wow','hooray','jolly']
    s = random.randint(0,3)
    print(f"computer choice: {s}")
    if a == s:
        print("TIE")
    elif a == 0 and s == 2 :
        print(f"{name} wins")
        u+=1
    elif s == 0 and a == 2:
        print(f"COMPUTER wins")
        c+=1
    elif s>a:
        print(f"COMPUTER wins")
        c+=1
    elif a>s:
        print(f"{name} wins")
        u+=1
    print("----SCORES----")
    print(f" COMPUTER: {c}         {name}: {u}")
