from collections import deque

class StaticClass:
    groupNum = 0
    DIR = [(0,-1),(0,1),(1,0),(-1,0)]
    _max = 0


def noWall(dx,dy,value):
    if (dx,dy) == (1,0):
        if value >= 8:
            return False
    if (dx,dy) == (-1,0):
        if value in (2,3,6,7,10,11,14,15):
            return False
    if (dx,dy) == (0,1):
        if value in (4,5,6,7,12,13,14,15):
            return False
    if (dx,dy) == (0,-1):
        if value in (1,3,5,7,9,11,13,15):
            return False

    return True



def initialCount(start,l,group,node):
    n,m = len(l),len(l[0])
    count = 1
    q = deque()
    q.append(start)

    node[start] = StaticClass.groupNum

    while q:
        x,y = q.popleft()
        for dx,dy in StaticClass.DIR:
            if dx+x>=0 and dx+x<n and dy+y>=0 and dy+y<m and (x+dx,dy+y) not in node and noWall(dx,dy,l[x][y]):
                node[(dx+x,dy+y)] = StaticClass.groupNum
                q.append((dx+x,dy+y))
                count+=1

    group[StaticClass.groupNum] = count
    StaticClass.groupNum += 1

def breakOne(start,l,group,node,visited):
    n,m = len(l), len(l[0])
    q = deque()
    q.append(start)
    visited[start]=True
    probe = {} # 탐색만한 것에 대해서
    _max = 0
    myGroup = node[start]
    totalRoom = group[myGroup]

    while q:
        x,y = q.popleft()
        for dx,dy in StaticClass.DIR:
            if x+dx>=0 and x+dx<n  and y+dy>=0 and y+dy<m and (x+dx,y+dy) not in visited and (x+dx,y+dy) not in probe:
                if noWall(dx,dy,l[x][y]):
                    visited[(x+dx,y+dy)]=True
                    q.append((x+dx,y+dy))
                else:
                    thisGroup = node[(x+dx,y+dy)]
                    if thisGroup == myGroup:
                        continue
                    thisTotalRoomCount = group[thisGroup]
                    if _max < thisTotalRoomCount:
                        _max = thisTotalRoomCount
                    probe[(x+dx,y+dy)]=True
    return _max + totalRoom













m,n = map(int,input().split())
l = [list(map(int,input().split())) for i in range(n)]

group = {} # 그룹의 방 개수를 담음
node = {} # 각각의 노드가 어떤 그룹에 속한지를 담음

for i in range(n):
    for j in range(m):
        if (i,j) not in node:
            # 방 개수 세기 및 가장 넓은 방 찾기 및 그룹 짓기
            initialCount((i,j),l,group,node)

visited = {}
for i in range(n):
    for j in range(m):
        if (i,j) not in visited:
            ret = breakOne((i,j),l,group,node,visited)
            if ret > StaticClass._max:
                StaticClass._max = ret

print(len(group))
nodes = list(group.items())
nodes.sort(key=lambda x:-x[1])
print(nodes[0][1])
print(StaticClass._max)
