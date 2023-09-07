from collections import deque
DIR = [(0,-1),(0,1),(1,0),(-1,0)]
n,m = map(int,input().split())
l = [input() for i in range(n)]
key,door= {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32},{'A':1,'B':2,'C':4,'D':8,'E':16,'F':32}
x,y = 0,0
for i in range(n):
    for j in range(m):
        if l[i][j] == '0':

            x,y = i,j
#abcdef 순서대로
visited = {(x,y,0):0}
q = deque([(x,y,0,0)])
answer = -1
while q:
    flag = False
    nx,ny,nk,nd = q.popleft()
    for dx,dy in DIR:
        # 지금 까지 간적이 없는 것은 보장이 된다
        if nx+dx>=0 and nx+dx<n and ny+dy>=0 and ny+dy<m and l[nx+dx][ny+dy] != '#' and (nx+dx,ny+dy,nk) not in visited:
            if l[nx+dx][ny+dy].isupper():
                if door[l[nx+dx][ny+dy]] & nk != 0:
                    visited[(nx+dx,ny+dy,nk)] = nd+1
                    q.append((nx+dx,ny+dy,nk,nd+1))
            elif l[nx+dx][ny+dy].islower():
                visited[(nx+dx,ny+dy, nk|key[l[nx+dx][ny+dy]] )] = nd+1
                q.append((nx+dx,ny+dy,nk|key[l[nx+dx][ny+dy]],nd+1))
            elif l[nx+dx][ny+dy] in ['.','0']:
                visited[(nx + dx, ny + dy, nk)] = nd + 1
                q.append((nx + dx, ny + dy, nk, nd + 1))

            elif l[nx+dx][ny+dy] == '1':
                answer = nd+1
                flag = True
                break
    if flag:
        break
print(answer)



