cost = int(50)
owe = int (0)

while cost > 0:
    x = int(input("insert a coin: "))
    if x not in (5, 10, 20, 25):
        print("amount due: ", cost)
    else: 
        cost = cost - x
        if cost < 0:
            owe = abs(cost)
            print ("change owed: ", owe)
        else:
            print ("amount due: ", cost)
