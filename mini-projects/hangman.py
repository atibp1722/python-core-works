import random
import string

from hangman_words import words

def getWord(words):
    word=random.choice(words)
    while('-' in word or ' ' in word):
        word=random.choice(words)
    return word.upper()

def playGame():
    word=getWord(words)
    word_letters=set(word) #stores the actual letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #stores letters the user has guessed 
    life=6

    while (len(word_letters)>0 and life>0) :
        print(f"You have {life} left")
        print("The letters already used for the word are: ",' '.join(used_letters))
        word_list=[letter if letter in used_letters else "_" for letter in word] #Display word in "W _ _ _ _ " format 
        print("Current word: ",' '.join(word_list))
        user_letter=input("Guess a letter: ").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                life=life-1
        elif user_letter in used_letters:
            print("Letter already guessed! Try again.")
        else:
            print("Invalid letter!! Try again.")
    if life==0:
        print("Sorry you died!! The word was:",word)
    else:
        print("You guessed the word:",word)

playGame()