from itertools import combinations as cb
import copy
from collections import deque
dir=[(0,-1),(0,1),(1,0),(-1,0)]
n,m,g,r = map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)] #0호수 1배양액 x 2배양액 ok
cand=[]
ans=[]
for i in range(n):
    for j in range(m):
        if l[i][j]==2:
            cand.append((i,j))
combi = list(cb(cand,r+g))
for i in combi:
    forRed=list(cb(i,r))
    for j in forRed:
        forGreen=[]
        for v in i:
            if v not in j:
                forGreen.append(v)
        l2=copy.deepcopy(l)
        visited={}
        q = deque()
        for x,y in forGreen:
            l2[x][y]="g"
            visited[(x,y)]=0
            q.append((x,y,"g",0))
        for x,y in j:
            l2[x][y]="r"
            visited[(x,y)]=0
            q.append((x,y,"r",0))
        count=0
        code=True


        while q:
            x,y,color,dist=q.popleft()
            if l2[x][y]==3:
                continue
            for dx,dy in dir:
                if x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<m and l2[x+dx][y+dy]!=0 and l2[x+dx][y+dy]!=3: #3이미 꽃
                    if color=="g" and l2[x+dx][y+dy]=="r" and visited[(x+dx,y+dy)]==dist+1:
                        count+=1
                        l2[x+dx][y+dy]=3
                    elif color=="r" and l2[x+dx][y+dy]=="g" and visited[(x+dx,y+dy)]==dist+1:
                        count+=1
                        l2[x+dx][y+dy]=3
                    elif color=="g" and (l2[x+dx][y+dy]==1 or l2[x+dx][y+dy]==2):
                        visited[(x+dx,y+dy)]=dist+1
                        l2[x+dx][y+dy]="g"
                        q.append((x+dx,y+dy,"g",dist+1))
                    elif color=="r" and (l2[x+dx][y+dy]==1 or l2[x+dx][y+dy]==2):
                        visited[(x+dx,y+dy)]=dist+1
                        l2[x+dx][y+dy]="r"
                        q.append((x+dx,y+dy,"r",dist+1))

        ans.append(count)
ans.sort(reverse=True)
print(ans[0])








