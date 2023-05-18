email=input("Enter a email address to check: ")
a=0
b=0
c=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for val in email:
                    if val==val.isspace():
                        a=1
                    elif val==val.isalpha():
                        if val==val.isupper():
                            b=1
                    elif val==val.isdigit():
                        continue
                    elif val=="_" or val=="@" or val==".":
                        continue
                    else:
                        c=1
                if a==1 or b==1 or c==1:
                    print("Email cannot have any spaces, uper case characters or any sepcial characters")
            else:
                print("'.' placement wrong in email")
        else:
            print("cannot have more than one '@' sign")
    else:
        print("First letter must always be a character")
else:
    print("Email entered isn't valid")