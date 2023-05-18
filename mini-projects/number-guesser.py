import random

def user_guess(n):
    random_num=random.randint(1,n)
    guess=0
    while(guess != random_num):
        guess=int(input(f"Enter a number to guess from {1} to {n}: "))
        if guess<random_num:
            print("Your guess is low.")
        elif guess>random_num:
            print("Your guess is high.")
    print(f"You guessed number {random_num} correctly!")

user_guess(10)

def cpu_guess(n):
    low_bound=1
    upper_bound=n
    cpu_answer=''
    while (cpu_answer != 'c') and (low_bound != upper_bound):
        guess=random.randint(low_bound, upper_bound)
        cpu_answer=input(f"Is {guess} too high (h), too low (h) or correct (c): ").lower()
        if cpu_answer=='l':
            low_bound=guess-1
        elif cpu_answer=='h':
            upper_bound=guess+1
    print(f"You guessed {guess} correctly!")

cpu_guess(10)


