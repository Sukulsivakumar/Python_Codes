import random
def computer():
    if len(lst) == 1:
        pe = lst[0]
        lst.pop(0)
        return pe
    else:
        l = len(lst)
        a = int(lst[0])
        b = int(lst[l - 1])
        if a > b:
            p = a
            lst.pop(0)
            return p
        else:
            u  = b
            lst.pop(l - 1)
            return u
def player():
    le = len(lst)
    ae = int(lst[0])
    be = int(lst[le - 1])
    if ae < be:
        if be > (int(lst[le - 2])):
            pe = be
            lst.pop(le - 1)
            return pe
        elif (int(lst[le - 2])) > be:
            if (int(lst[le - 2])) > (int(lst[1])):
                pe = int(lst[0])
                lst.pop(0)
                return pe
            elif (int(lst[le - 2])) < (int(lst[1])):
                pe = be
                lst.pop(le - 1)
                return pe
    elif ae > be:
        if ae > (int(lst[1])):
            ue = ae
            lst.pop(0)
            return ue
        elif ae < (int(lst[1])):
            if (int(lst[1])) > (int(lst[le - 2])):
                ue = int(lst[le - 1])
                lst.pop(le - 1)
                return ue
            elif (int(lst[1])) < (int(lst[le - 2])):
                ue = int(lst[0])
                lst.pop(0)
                return ue
name = input("Enter your Name: ")
lst = []
for i in range(0, 10):
    lst.append(random.randint(1,100))
print(lst)
c = r = 0
while True:
    z = player()
    r = r + z
    v = computer()
    c = c + v
    print("----------------------------------------------------------------------------------------------------------------------------")
    print(f"{name} shoot {z}")
    print(f"Computer shoot {v}")
    print(f"Total {name} shoots {r}")
    print(f"Total Computer shoots {c}")

    print("----------------------------------------------------------------------------------------------------------------------------")
    print(lst)
    if len(lst) == 0:
        if c > r:
            print("Computer Wins")
        else:
            print(f"{name} Wins")
        break
