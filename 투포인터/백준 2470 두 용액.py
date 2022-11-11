n=int(input())
l=list(map(int,input().split()))
l.sort()
x,y=0,0
comp=10000000000
start=0
end=len(l)-1
while True:
    if start+1==end:
        if abs(l[start]+l[end])<comp:
            x,y=l[start],l[end]
        break

    target=l[start]+l[end]
    if abs(target)<comp:
        comp=abs(target)
        x,y=l[start],l[end]
    if target==0:
        break
    if target>0:
        end-=1
    else:
        start+=1
print(x,y)
