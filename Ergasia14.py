a = int(input("Give number a "))
b = int(input("Give number b "))
d = int(input("Give number d "))
y=[]
x=0
#prwta bazw se mia lista olous tus prwthoys arithmous
for i in range(a,b+1):
    count=0

    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:

        y.append(i)
        x = x + 1



#edw tsekarw thn lista me tous prwtous arithmous ana zeygaria
for num in range(0,x-1):
    if abs(y[num]-y[num+1])==d:
         print(y[num],y[num+1])
         break