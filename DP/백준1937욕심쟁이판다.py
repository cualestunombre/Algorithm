import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
global n
n = int(input())
dir=[(-1,0),(0,-1),(1,0),(0,1)]
l = [list(map(int,input().split())) for i in range(n)]
def dp(x):
    global n
    if x in cache:
        return cache[x]
    i,j = x
    candidate=[]
    for u,v in dir:
        if i + u >= 0 and i + u < n and j + v >= 0 and j + v < n:
            if l[i+u][j+v]>l[i][j]:
                candidate.append(dp((i+u,j+v))+1)
    if len(candidate) == 0 :
        cache[x] = 1

    else:
        candidate.sort(reverse=True)
        cache[x]=candidate[0]
    return cache[x]




min=0
cache={}
for i in range(n):
    for j in range(n):
        if (i,j) not in cache:
            dp((i,j))
        if cache[(i,j)] >min:
            min=cache[(i,j)]
print(min)





