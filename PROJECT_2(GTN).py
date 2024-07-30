import random
n = random.randint(0,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the correct no : "))
    if(a<n):
        print("Higher number please")
        guesses +=1
    elif(a>n):
        print("Lower number please")
        guesses +=1
print(f" you have guess the number {a} in {guesses} attempts")
