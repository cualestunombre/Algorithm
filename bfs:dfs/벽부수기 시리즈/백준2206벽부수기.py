from collections import deque
import sys
n,m = map(int,input().split())
l=[ sys.stdin.readline() for i in range(n)]

visited={}
q=deque([(0,0,0)]) #한번 부수고 온 놈은 1에 못들어간다 한번 부수고 온 놈은 다음 곳에 들어갈 때 표식을 남긴다
# 안 부순 놈은 한번 부술 수도 있고 안부 술 수도 있다
visited[(0,0,0)]=1
direction=[(0,-1),(1,0),(-1,0),(0,1),]
while q:
    x,y,z=q.popleft()
    if z==0:
        for dx,dy in direction:
            if x+dx>=0 and x+dx<=n-1 and y+dy>=0 and y+dy<=m-1:
                if l[x+dx][y+dy]=='1' and (x+dx,y+dy,1) not in visited:
                    q.append((x+dx,y+dy,1))
                    visited[(x+dx,y+dy,1)]=visited[(x,y,z)]+1
                elif l[x+dx][y+dy]=='0' and (x+dx,y+dy,0) not in visited:
                    q.append((x+dx,y+dy,0))
                    visited[(x + dx, y + dy, 0)] = visited[(x, y, z)] + 1
    else:
        for dx,dy in direction:
            if x+dx>=0 and x+dx<=n-1 and y+dy>=0 and y+dy<=m-1:
                if l[x+dx][y+dy]=='0' and (x+dx,y+dy,0) not in visited and (x+dx,y+dy,1) not in visited:
                    q.append((x+dx,y+dy,1))
                    visited[(x + dx, y + dy, 1)] = visited[(x, y, z)] + 1

x=10000000
y=10000000
if (n-1,m-1,0) in visited:
    x=visited[(n-1,m-1,0)]
if (n - 1, m - 1, 1) in visited:
    y = visited[(n - 1, m - 1, 1)]
if x==10000000 and y==10000000:
    print(-1)
else:
    print(min(x,y))





