import random
a=[[0,0,0],[0,0,0],[0,0,0]]
won=False
l=0
turn=1
while won==False and l<9:

    put=False
    l += 1
#to number tha antistoixei se ena koutaki sthn triliza| prwth grammh(1-3) |deyterh grammh(4-6) |trith grammh(7-9)|
    while put==False:
        if turn % 2 != 0:
            number = int(input("Give position (1-9) "))
        else:
            number = random.randint(1, 9)
        x = 0
        for i in range(0,3):
            for j in range (0,3):
                x+=1
                if number==x:
                    if a[i][j]==0:
                        if turn%2!=0:
                            a[i][j]=1
                        else:
                            a[i][j]=2
                        if turn%2!=0:
                            print("You chose", x)
                        else:
                            print("Pc chose", x)
                        put=True
                        turn+=1



        if put==False and turn % 2 != 0:
            print("Choose another position ")

    for i in range(0,3):
        p1=0
        p2=0
        for j in range (0,3):
            if a[i][j]==1:
                p1+=1
            elif a[i][j]==2:
                p2+=1
        if p1==3:
            winner=1
            won=True
        elif p2==3:
            winner=2
            won=True

    if won==False:
        for j in range(0,3):
            p1=0
            p2=0
            for i in range(0,3):
                if a[i][j]==1:
                    p1+=1
                elif a[i][j]==2:
                    p2+=1
            if p1==3:
                won=True
                winner=1
            elif p2==3:
                won=True
                winner=2

    if won==False:
        p1=0
        p2=0
        for i in range(0,3):
            if a[i][i]==1:
                p1+=1
            elif a[i][i]==2:
                p2+=1
        if p1 == 3:
            won = True
            winner = 1
        elif p2 == 3:
            won = True
            winner = 2

    if won==False:
       p1=0
       p2=0
       for i in range(0,3):
           for j in range (0,3):
               if i+j==2:
                   if a[i][j]==1:
                       p1+=1
                   elif a[i][j]==2:
                       p2+=1
       if p1 == 3:
           won = True
           winner = 1
       elif p2 == 3:
           won = True
           winner = 2


if won==True:
    if winner==1:
        print("You Won")
    else:
        print("Pc Won")
else:
    print("No Winner")


