n ,m = map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
cache={}
dir=[(-1,0),(1,0),(0,1),(0,-1)]
def dp(x,y):
    if x==n-1 and y==m-1:
        return 1
    summ=0
    for dx,dy in dir:
        if x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<m:
            if l[x+dx][y+dy]<l[x][y]:
                if(x+dx,y+dy) in cache:
                    summ+=cache[(x+dx,y+dy)]
                else:
                    summ+=dp(x+dx,y+dy)
    cache[(x,y)]=summ
    return summ
print(dp(0,0))


