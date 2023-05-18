import random
print("----------------------WELCOME TO THE QUIZ----------------------")
q1="Which is not a data structure type?\na)Queue\nb)Stack\nc)List\nd)Tree"
q2="Which is a data valid python framework?\na)Mango\nb)Django\nc)Flask\nd)Both c and d"
q3="Which is data structure type?\na)Tree\nb)Branch\nc)Root\nd)Leaf"
q4="What type of pragramming language is pythpn??\na)Structured\nb)Maybe Both\nc)OOP\nd)Procedural"
q5="Which is not a prgramming language?\na)C\nb)Selerium\nc)Java\nd)Ruby"

answers={q1:"c",q2:"d",q3:"a",q4:"c",q5:"b"}
total=0
for val in answers:
    val=random.choice(list(answers.keys()))
    print(val)
    ans=input("Enter your answer a/b/c/d: ")
    ans=ans.lower()
    if ans==answers[val]:
        print("Yay! you got it right.")
        total+=1
    else:
        print("Oops! You guessed incorrect.")
print("Your total is:", total)

for data in answers.values():
    print("Correct answer:",data)