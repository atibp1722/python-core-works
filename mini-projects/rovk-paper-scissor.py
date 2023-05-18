import random

user_score=0
cpu_score=0

choices=['r','p','s']

while True:
    user_input=input("Rock(r) Paper(p) Scissor(s) OR Quit (q) to quit: ").lower()
    if user_input=='q':
        quit()
    if user_input not in choices:
        continue
    random_num=random.randint(0,2)
    cpu_guess=choices[random_num]
    print("CPU chose:",cpu_guess)

    if user_input=='r' and cpu_guess=='s':
        print("User wins.")
        user_score=user_score+1   
    elif user_input=='p' and cpu_guess=='r':
        print("User wins")
        user_score=user_score+1
    elif user_input=='s' and cpu_guess=='p':
        print("User wins")
        user_score=user_score+1
    else:
        print("CPU wins.")
        cpu_score=cpu_score+1
    print(f"User won {user_score} times")
    print(f"CPU won {cpu_score} times")
    print("Thank you for playing")
