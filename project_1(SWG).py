import random
computer=random.choice([0,1,-1])
yourstr=input("enter your move:")
yourdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=yourdict[yourstr]

print(f"your move is {reversedict[you]} and computer move is {reversedict[computer]}")

if(computer==you):
    print("the match is a draw")
else:

    if(computer==1 and you==-1):
        print("you lose")
    
    elif(computer==1 and you==0):
        print("you won")
    
    elif(computer==-1 and you==1):
        print(" you won ")
    
    elif(computer==-1 and you==0):
        print(" you lose ")
    
    elif(computer==0 and you==1):
        print(" you lose ")
    
    elif(computer==0 and you==-1):
        print(" you won ")
    
    else:
        print("something went wrong")
   