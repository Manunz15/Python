i=0
j=0
k=0

a=[]
b=[]
c=[]

n=100
m=100
p=100

while n>16:
    n=int(input("Quante righe ha la matrice A? (Max 16)\n"))
while p>16:
    p=int(input("Quante colonne ha la matrice A? (Max 16)\n"))
while m>16:
    m=int(input("Quante colonne ha la matrice B? (Max 16)\n"))

for i in range(n):
    a.append([0]*p)
for i in range(p):
    b.append([0]*m)
for i in range(n):
    c.append([0]*m)

for i in range(n):
    for j in range(p):
        print("a",i,j,end='')
        a[i][j]=int(input("="))

for i in range(p):
    for j in range(m):
        print("b",i,j,end='')
        b[i][j]=int(input("="))

for i in range(n):
    for j in range(m):
        for k in range(p):
            c[i][j]+=a[i][k]*b[k][j]

print("\nA\n")
for i in range(n):
    print("|", end=' ')
    for j in range(p):
        print(a[i][j],end=' ')
    print("|",sep='')

print("\nB\n")
for i in range(p):
    print("|", end=' ')
    for j in range(m):
        print(b[i][j],end=' ')
    print("|",sep='')

print("\nC\n")
for i in range(n):
    print("|", end=' ')
    for j in range(m):
        print(c[i][j],end=' ')
    print("|",sep='')