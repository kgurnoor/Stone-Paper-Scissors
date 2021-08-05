from random import randint
p=("Y")
while p==("Y"):

    a= input("stone, paper, scissors? ")
    l=['stone','paper', 'scissors']
    c=l[randint(0,2)]

    if a== ("stone") and c==("paper"):
        result= ("computer wins")
    elif a==("paper") and c==("scissors"):
        result=("computer wins")
    elif a==("scissors") and c==  ("stone"):
        result=  ("computer wins")
    elif a==("stone") and c==("scissors")  :
        result= ("you win")
    elif a==("paper") and c== ("stone") :
        result=  ("you win")
    elif a==("scissors") and c==("paper")  :
        result= ("you win")
    elif a==c:
        result=("draw")
    else:
        result=("invalid")
    print("you chose- ",a, "computer chose- ", c,"\n result is ", result  )
    p=input("next game?(Y/N)")
