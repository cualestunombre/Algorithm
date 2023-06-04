from collections import deque
dir = [(0,-1),(0,1),(1,0),(-1,0)]
def check(key,lock,x,y,unlockPoint):
    count = 0
    m = len(key)
    n = len(lock)
    for dx in range(m):
        for dy in range(m):
            if x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<n :
                if lock[x+dx][y+dy] == 0 and key[dx][dy] == 1:
                    count+=1
                elif lock[x+dx][y+dy] == 1 and key[dx][dy] == 0:
                    pass
                else:
                    return False

    return count==unlockPoint
def assgin(key,lock,unlockPoint):
    m = len(key) #키의 사이즈
    n = len(lock) #자물쇠의 사이즈
    q = deque()
    q.append((0,0))
    visited  = {(0,0):True}
    while q:
        x,y = q.pop()
        if check(key,lock,x,y,unlockPoint):
            return True
        for dx,dy in dir:
            if dy+y>-m and dy+y<n and dx+x>-m and dx+x<n and (dx+x,dy+y) not in visited:
                q.append((dx+x,dy+y))
                visited[(dx+x,dy+y)]=True
    return False

def clockWiseRoate(key):
    m = len(key)
    l = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m-1,-1,-1):
            l[i].append(key[j][i])
    key[:] = l

def solution(key, lock):
    unlockPoint = 0
    for _ele in lock:
        for __ele in _ele:
            if __ele == 0:
                unlockPoint+=1
    flag1 = assgin(key , lock,unlockPoint)
    clockWiseRoate(key)
    flag2 = assgin(key,lock,unlockPoint)
    clockWiseRoate(key)
    flag3 = assgin(key,lock,unlockPoint)
    clockWiseRoate(key)
    flag4 = assgin(key,lock,unlockPoint)
    return flag1 or flag2 or flag3 or flag4

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

