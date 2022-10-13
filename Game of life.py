import random
import time

screen=[]
old=[]
i=0
j=0
k=0
nrow=28
ncol=70
gen=50
life=0

def death():
    life=0
    if(i==0 and j==0):
        life+=old[i][j+1]
        life+=old[i+1][j]
        life+=old[i+1][j+1]
    elif(i==0 and j==ncol-1):
        life+=old[i][j-1]
        life+=old[i+1][j-1]
        life+=old[i+1][j]
    elif(i==nrow-1 and j==0):
        life+=old[i-1][j]
        life+=old[i-1][j+1]
        life+=old[i][j+1]
    elif(i==nrow-1 and j==ncol-1):
        life+=old[i-1][j-1]
        life+=old[i-1][j]
        life+=old[i][j-1]
    elif i==0:
        life+=old[i][j-1]
        life+=old[i][j+1]
        life+=old[i+1][j-1]
        life+=old[i+1][j]
        life+=old[i+1][j+1]
    elif i==nrow-1:
        life+=old[i][j-1]
        life+=old[i][j+1]
        life+=old[i-1][j-1]
        life+=old[i-1][j]
        life+=old[i-1][j+1]
    elif j==0:
        life+=old[i-1][j]
        life+=old[i+1][j]
        life+=old[i-1][j+1]
        life+=old[i][j+1]
        life+=old[i+1][j+1]
    elif j==ncol-1:
        life+=old[i-1][j]
        life+=old[i+1][j]
        life+=old[i-1][j-1]
        life+=old[i][j-1]
        life+=old[i+1][j-1]
    else:
        life+=old[i-1][j-1]
        life+=old[i-1][j]
        life+=old[i-1][j+1]
        life+=old[i][j-1]
        life+=old[i][j+1]
        life+=old[i+1][j-1]
        life+=old[i+1][j]
        life+=old[i+1][j+1]
    return life



for i in range(nrow):
    screen.append([0]*ncol)
    old.append([0]*ncol)

i=0

for i in range(nrow):
    j=0
    while(j<ncol):
        screen[i][j]=random.randrange(0, 2)
        old[i][j]=screen[i][j]
        j+=1

i=0

for k in range(gen):
    print("\n\nGenerazione ", end='')
    print(k+1)
    for i in range(nrow):
        j=0
        while(j<ncol):
            if screen[i][j]==0:
                print(" ", end='')
            else:
                print("0", end='')
            j+=1
        print(sep='')
   
    i=0
    for i in range(nrow):
        j=0
        while(j<ncol):
            life=death()
            if life==3:
                screen[i][j]=1
            elif(life<2 or life>3):
                screen[i][j]=0
            j+=1

    i=0
    for i in range(nrow):
        j=0
        while(j<ncol):
            old[i][j]=screen[i][j]
            j+=1


    time.sleep(1)