import string, random

chars=list(string.ascii_letters+string.digits+"!@#$%^&*")

def generateRandomPassword():
    pass_length=int(input("Enter desired length of password: "))
    if pass_length<6:
        print("Length must be greater than 6")
        quit()
    
    random.shuffle(chars)

    generated_password=[]
    for val in range(pass_length):
        generated_password.append(random.choice(chars))

    random.shuffle(generated_password)

    generated_password="".join(generated_password)
    
    print(generated_password)

option=input("Do you wish to generate a password? [y/n]: ").lower()
if option=='y':
    generateRandomPassword()
elif option=='n':
    print("Thank you and goodbye")
    quit()
else:
    print("Invalid optin chosen")