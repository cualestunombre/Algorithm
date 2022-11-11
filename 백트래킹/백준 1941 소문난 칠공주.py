global count
from collections import deque
count=0
direction=[(0,-1),(0,1),(1,0),(-1,0)]
info=[input() for i in range(5)]
def bfs(l):
    q=deque()
    q.append(l[0])
    visited={l[0]:True}
    while q:
        x,y = q.popleft()
        for dx,dy in direction:
            if dx+x>=0 and dx+x<5 and dy+y>=0 and dy+y<5:
                if (dx+x,dy+y) in l and (dx+x,dy+y) not in visited:
                    q.append((dx+x,dy+y))
                    visited[(dx+x,dy+y)]=True
    if len(visited)==7:
        return True
    else:
        return False


def search(i,j,l):
    global count
    sCount = 0
    yCount = 0
    for x,y in l:
        if info[x][y]=='S':
            sCount+=1
        else:
            yCount+=1

    if sCount+yCount==7 and sCount>=4:
        if bfs(l):
            count+=1
        return
    if yCount>=4 or (sCount+yCount)>=7 or (i==4 and j==4):
        return

    if j == 4 and i + 1 < 5:
        l.append((i+1,0))
        search(i + 1, 0, l)
    elif j < 4:
        l.append((i, j + 1))
        search(i, j + 1, l)
    if l:
        l.pop()
    if j == 4 and i + 1 < 5:
        search(i + 1, 0, l)
    elif j < 4:
        search(i, j + 1, l)
    #취할 수도 아닐 수도 있음

    return



l=[(0,0)]
search(0,0,l)
l=[]
search(0,0,l)
print(count)


