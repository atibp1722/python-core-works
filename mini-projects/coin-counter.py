amt=float(input("Enter amount: "))

change=(int)(amt*100)
print("Amount in paisa is:",change)

coin_counter=0
while(change>=50):
    change=change-50
    coin_counter+=1
while(change>=25):
    change=change-25
    coin_counter+=1
while(change>=10):
    change=change-10
    coin_counter+=1
while(change>=5):
    change=change-5
    coin_counter+=1
while(change>=2):
    change=change-2
    coin_counter+=1
while(change>=1):
    change=change-1
    coin_counter+=1
print("The total number of coins for Rs.",amt,"is",coin_counter)