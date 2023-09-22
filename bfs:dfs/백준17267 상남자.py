from collections import deque
n,m = map(int,input().split())
l,r = map(int,input().split())
visited = [[-1 for i in range(m)] for j in range(n)]
mm = [ input() for i in range(n)]
x,y = 0,0
for i in range(n):
    for j in range(m):
        if mm[i][j] == "2":
            x,y = i,j
visited[x][y] = (l,r)
q = deque([(x,y,l,r)])
DIR = [(0,-1),(1,0),(-1,0),(0,1)]
while q:
    nx,ny,nl,nr = q.popleft()
    for dx,dy in DIR:
        if nx+dx>=0 and nx+dx<n and ny+dy>=0 and ny+dy<m and mm[nx+dx][ny+dy]!='1' and visited[nx+dx][ny+dy] == -1:
            if (dx,dy) == (1,0) or (dx,dy) == (-1,0):
                q.append((nx+dx,ny+dy,nl,nr))
                visited[nx+dx][ny+dy] = (nl,nr)
            elif (dx,dy) == (0,1) and nr-1>=0:
                q.append((nx+dx,ny+dy,nl,nr-1))
                visited[nx + dx][ny + dy] = (nl,nr-1)
            elif (dx,dy) == (0,-1) and nl-1>=0:
                q.append((nx + dx, ny + dy, nl-1, nr))
                visited[nx + dx][ny + dy] = (nl-1,nr)
        elif nx+dx>=0 and nx+dx<n and ny+dy>=0 and ny+dy<m and mm[nx+dx][ny+dy]!='1' and visited[nx+dx][ny+dy] != -1:
            if (dx,dy) == (1,0) or (dx,dy) == (-1,0) and (visited[nx+dx][ny+dy][0] < nl or visited[nx+dx][ny+dy][1] < nr ):
                q.append((nx+dx,ny+dy,nl,nr))
                visited[nx+dx][ny+dy] = (nl,nr)
            elif (dx,dy) == (0,1) and nr-1>=0 and (visited[nx+dx][ny+dy][1] < nr-1 ):
                q.append((nx+dx,ny+dy,nl,nr-1))
                visited[nx + dx][ny + dy] = (nl,nr-1)
            elif (dx,dy) == (0,-1) and nl-1>=0 and  (visited[nx+dx][ny+dy][0]<nl-1):
                q.append((nx + dx, ny + dy, nl-1, nr))
                visited[nx + dx][ny + dy] = (nl-1,nr)

count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] != -1:
            count +=1
print(count)
