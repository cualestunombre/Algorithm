n=int(input())
l=list(map(int,input().split()))
l.sort()
x,y,z=0,0,0
comp=10000000000
for i in range(len(l)-2):
    a=i
    b=i+1
    c=len(l)-1
    while True:
        if b==c:
            break
        target=l[a]+l[b]+l[c]
        if abs(target)<comp:
            comp=abs(target)
            x,y,z=l[a],l[b],l[c]
        if target==0:
            break
        elif target>0:
            c-=1
        else:
            b+=1
print(x,y,z)