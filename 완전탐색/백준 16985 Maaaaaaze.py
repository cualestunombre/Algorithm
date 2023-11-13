from itertools import permutations
from collections import  deque
import copy
DIR = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
cand,cache = [],{}
l = [[list(map(int,input().split())) for __ in range(5)] for _ in range(5)]

def generate(temp):
    if len(temp) == 5:
        cand.append(tuple(temp))
        return
    for _ in range(4):
        temp.append(_)
        generate(temp)
        temp.pop()

def clock_wise(l):
    temp = [[0 for __ in range(5)] for _ in range(5)]
    for _ in range(5):
        for __ in range(5):
            temp[_][4-__] = l[__][_]
    return temp

def rotate(index ,count):
    if (index,count) in cache:
        return cache[(index,count)]
    if count == 0:
        cache[(index,count)] = copy.deepcopy(l[index])
        return cache[(index,count)]
    else:
        ret = rotate(index,count-1)
        cache[(index,count)] = clock_wise(ret)
        return cache[(index,count)]

def bfs(target):
    if target[0][0][0] == 0:
        return 10**200
    start = (0,0,0)
    q = deque([start])
    visited = [[[-1 for i in range(5)] for j in range(5)] for k in range(5)]
    visited[0][0][0] = 0
    while q:
        z,x,y = q.popleft()
        d = visited[z][x][y]
        for dz,dx,dy in DIR:
            if z+dz>=0 and z+dz<5 and x+dx>=0 and x+dx<5 and y+dy>=0 and y+dy<5 and visited[z+dz][x+dx][y+dy] == -1 \
                    and target[z+dz][x+dx][y+dy] == 1 :
                visited[z+dz][x+dx][y+dy] = d + 1
                q.append((z+dz,x+dx,y+dy))
    if visited[4][4][4] != -1:
        return visited[4][4][4]
    else:
        return 10**200


generate([])
answer = 10**200
# 0,1,2,3,4의 순열 생성
seqs = list(permutations([0,1,2,3,4]))
for seq in seqs:
    for a,b,c,d,e in cand:
        target = []
        target.append(rotate(seq[0],a))
        target.append(rotate(seq[1],b))
        target.append(rotate(seq[2],c))
        target.append(rotate(seq[3],d))
        target.append(rotate(seq[4],e))
        answer = min(bfs(target),answer)

if answer == 10**200:
    print(-1)
else:
    print(answer)


