import random
a=list(input("Enter your names: ").split(","))
print(f"{a[random.randint(0,(len(a)-1))]} will pay the bill")
