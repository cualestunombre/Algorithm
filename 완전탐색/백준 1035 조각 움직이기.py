from itertools import combinations,permutations
from collections import deque
DIR = [(0,-1),(0,1),(1,0),(-1,0)]
def bfs(cand):
    start = cand[0]
    visited = {start:True}
    q = deque([start])
    while q:
        x,y = q.popleft()
        for dx,dy in DIR:
            if (x+dx,y+dy) in cand and (x+dx,y+dy) not in visited:
                visited[(x+dx,y+dy)] = True
                q.append((x+dx,y+dy))
    if len(visited) == len(cand):
        return True
    return False

def cal(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


l = [input() for _ in range(5)]
component = []
for row in range(5):
    for col in range(5):
        if l[row][col] == '*':
            component.append((row,col))

cands = []
for _ in range(5):
    for __ in range(5):
        cands.append((_,__))

cands = list(combinations(cands,len(component)))

targets = []
for cand in cands:
    if bfs(cand):
        targets.append(cand)

sequences = list(permutations(component))
ret = 10**100
for sequence in sequences: # player 들의 순서
    for target in targets: #
        value = 0
        for index,player in enumerate(sequence):
            value += cal(player,target[index])
        ret = min(ret,value)
print(ret)
