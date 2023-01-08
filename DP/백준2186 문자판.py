dir=[(0,-1),(0,1),(1,0),(-1,0)]
def check(u,v):
    if u>=0 and u<n and v>=0 and v<m:
        return True
    return False
def dp(i,j,num):
    if num==rep:
        return 1
    cnt=0
    for v in range(1,k+1):
        for x,y in dir:
            if check(i+x*v,j+y*v) and strings[i+x*v][j+y*v]==target[num+1]:
                if (i+x*v,j+y*v,num+1) in cache:
                    cnt+=cache[(i+x*v,j+y*v,num+1)]
                else:
                    cnt+=dp(i+x*v,j+y*v,num+1)
    cache[(i,j,num)]=cnt
    return cnt




n,m,k = map(int,input().split())
count=0
strings=[]
cache={}
for i in range(n):
    strings.append(input())
target=input()
rep=len(target)-1
for i in range(n):
    for j in range(m):
        if target[0]==strings[i][j]:
            count+=dp(i,j,0)
print(count)