def billing(i):
    while True:
        print("\n\n\t\tKARUR TIFFUN CENTER")
        while i<9999:
            print("Bill Number: ",i)
            i+=1
            break
        
        print("\n\tMENU\n1. Dosa Rs.25\n2. Idly Rs.10\n3. Pongal Rs.40\n4. Poori Rs.13")
        print("Select The Food")
        #n= int(input("Enter the Dish Number: "))
        lst = []
        n = int(input("Enter the Number of Dishes: "))
        for i in range(0, n):
                ele = int(input("Enter the Dish Number: "))
                lst.append(ele)
        m=0
        j=[]
        while m<n:
            
            match lst[m]:
                case 1:
                    dosa=int(input("Enter Dosa Quantity: "))
                    do=dosa*25
                    j.append(do)
                case 2:
                    idly=int(input("Enter Idly Quantity: "))
                    i_d=idly*10
                    j.append(i_d)
                case 3:
                    pongal=int(input("Enter Pongal Quantity: "))
                    po=pongal*40
                    j.append(po)
                case 4:
                    poori=int(input("Enter Poori Quantity: "))
                    pr=poori*13
                    j.append(pr)
                case _:
                    print("PLEASE SELECT A DISH")
            m+=1
        h=0
        for f in range(0,n):
            h+=j[f]
        print("")
        print("--------------------------------------------------")
        print("Total Price: ",h)
        print("--------------------------------------------------")
        break
    return i

i=1000
while True:
    print("\n\n1. Billing\n2.Exit")
    bill= int(input("select the option: "))
    if bill==1:
        billing(i)
        i+=1
    elif bill==2:
        print("THANK YOU")
        break
    else:
        print("INVALID CAMMAND")
    
    
