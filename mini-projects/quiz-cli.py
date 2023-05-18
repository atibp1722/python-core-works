
print("--------------------WELCOME TO THE QUIZ--------------------")
life=1
choices=["a","b","c","d"]
total=0

q1=print("What is the capital of Nepal?\na)Kathmandu\nb)Lalitpur\nc)Pokhara\nd)Chitwan")
correct_q1="a"

for val in range(life):
    answer=input("Enter your choice a/b/c/d: ")
    answer=answer.lower()
    if answer in choices:
        if answer==correct_q1:
            print("Your answer is correct")
            total+=1
            break
        else:
            print("The answer is incorrect")
    else:
        print("Incorrect option chosen")

q2=print("Who won the FIFA Mens World Cup in 2022?\na)France\nb)Brazil\nc)Argentina\nd)Spain")
correct_q2="c"

for val in range(life):
    answer=input("Enter your choice a/b/c/d: ")
    answer=answer.lower()
    if answer in choices:
        if answer==correct_q2:
            print("Your answer is correct")
            total+=1
            break
        else:
            print("The answer is incorrect")
    else:
        print("Incorrect option chosen")

q3=print("What type of language is python?\na)Strcutured\nb)OOP\nc)None\nd)Both a and b")
correct_q3="b"

for val in range(life):
    answer=input("Enter your choice a/b/c/d: ")
    answer=answer.lower()
    if answer in choices:
        if answer==correct_q3:
            print("Your answer is correct")
            total+=1
            break
        else:
            print("The answer is incorrect")
    else:
        print("Incorrect option chosen")

q4=print("Which are python libraries?\na)String\nb)Math\nc)Document\nd)Both a and b")
correct_q4="d"

for val in range(life):
    answer=input("Enter your choice a/b/c/d: ")
    answer=answer.lower()
    if answer in choices:
        if answer==correct_q4:
            print("Your answer is correct")
            total+=1
            break
        else:
            print("The answer is incorrect")
    else:
        print("Incorrect option chosen")

q5=print("Which of the follwing doesnt exist in python?\na)Break\nb)While\nc)If Else\nd)Do While")
correct_q5="d"

for val in range(life):
    answer=input("Enter your choice a/b/c/d: ")
    answer=answer.lower()
    if answer in choices:
        if answer==correct_q5:
            print("Your answer is correct")
            total+=1
            break
        else:
            print("The answer is incorrect")
    else:
        print("Incorrect option chosen")
print("")
print("Final Score is:", total)

print("The correct answeers are:",correct_q1, correct_q2, correct_q3, correct_q4, correct_q5)

if total<2:
    print("You suck")
elif total>=2 and total <=3:
    print("You are avarage")
else:
    print("You did excellent")