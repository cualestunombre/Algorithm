import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
n=int(input())
l=list(map(int,input().split()))
l.insert(0,0)
adj={}
for i in range(n-1):
    x,y=map(int,input().split())
    if x in adj:
        adj[x].append(y)
    else:
        adj[x]=[y]
    if y in adj:
        adj[y].append(x)
    else:
        adj[y]=[x]
cache={}
def dp(number,selected,caller):
    if (number,selected) in cache:
        return cache[(number,selected)]
    if selected==True: #우수마을일 시
        temp=0
        for i in adj[number]:
            if i!=caller:
                temp += dp(i,False,number)
        cache[(number,selected)]=temp+l[number]
        return cache[(number,selected)]
    else:
        temp=0
        for i in adj[number]:
            if i!=caller:
                a=dp(i,False,number)
                b=dp(i,True,number)
                temp+=max(a,b)
        cache[(number,selected)]=temp
        return cache[(number,selected)]


a=dp(1,True,0)
b=dp(1,False,0)
print(max(a,b))