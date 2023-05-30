import copy
from collections import deque
global answer
global round
round=0
answer=[]
#가장 약한 포탑을 찾는 함수
def findWeakest(l,attacked):
    basket = []
    n = len(l)
    m = len(l[0])
    x,y=(0,0)
    for i in range(n):
        for j in range(m):
            if l[i][j]==0:
                continue
            basket.append((i,j,l[i][j]))
    basket.sort(key=lambda x:(x[2],-attacked[(x[0],x[1])],-(x[0]+x[1]),-x[1]))
    return (basket[0][0],basket[0][1])
#가장 강한 포탑을 찾는 함수
def findStrongest(l,attacked):
    basket = []
    n = len(l)
    m = len(l[0])
    x,y=(0,0)
    for i in range(n):
        for j in range(m):
            if l[i][j]==0:
                continue
            basket.append((i,j,l[i][j]))
    basket.sort(key=lambda x:(-x[2],attacked[(x[0],x[1])],(x[0]+x[1]),x[1] ))
    return (basket[0][0],basket[0][1])
# 부서진 포탑의 개수를 세는 함수
def countAlive(l):
    count=0
    n=len(l)
    m=len(l[0])
    for i in range(n):
        for j in range(m):
            if l[i][j]!=0:
                count+=1
    return count
# 시작 헬퍼 함수
def initialize(attacked,l):
    n=len(l)
    m=len(l[0])
    for i in range(n):
        for j in range(m):
            if l[i][j]!=0:
                attacked[(i,j)]=0
#포탑 정비 함수
def cure(participated,l):
    n=len(l)
    m=len(l[0])
    for i in range(n):
        for j in range(m):
            if l[i][j]!=0 and (i,j) not in participated:
                l[i][j]+=1
# bfs 함수
def handleBfs(l, start, target):
    n=len(l)
    m=len(l[0])
    global round
    global answer
    q=deque()
    visited={start:True}
    can_reach=False
    q.append(start)
    while q:
        x,y=q.popleft()
        for dx,dy in dir:
            tx=x+dx
            ty=y+dy
            if tx>=n:
                tx=tx%n
            elif tx<0:
                tx=n+tx

            if ty>=m:
                ty=ty%m
            elif ty<0:
                ty=m+ty
            if (tx,ty) not in visited and l[tx][ty]!=0:
                q.append((tx,ty))
                visited[(tx,ty)]=(x,y)
                if (tx, ty) == target:
                    can_reach = True
                    visited[(tx, ty)] = (x, y)
                    break
        if can_reach:
            break
    if can_reach:
        cur=target

        while True:
            answer.append(visited[cur])
            cur=visited[cur]
            if cur==True:
                answer.pop()
                break
    return





# 레이저 공격 함수
def laserAttack(l, participated, w, s, power):
    global answer
    answer = []
    flag = False  # 경로 찾은 여부
    ways = [w]
    handleBfs(l, w, s)

    if len(answer) != 0:
        flag = True
    if not flag:
        return False
    attack(l, s, power)
    for x, y in answer:
        if (x, y) != w and (x, y) != s:
            participated[(x, y)] = True
            attack(l, (x, y), power // 2)
    return True

#공격함수
def attack(l,defender,damage):
    if l[defender[0]][defender[1]]<=damage:
        l[defender[0]][defender[1]]=0
    else:
        l[defender[0]][defender[1]]-=damage

#포탄공격함수
def shellAttack(l,participated,w,s,power):
    n=len(l)
    m=len(l[0])
    attack(l,s,power)
    shellDir = [(0,-1),(0,1),(1,0),(-1,0),(-1,1),(-1,-1),(1,-1),(1,1)]
    for dx,dy in shellDir:
        sx,sy=s
        tx = sx+dx
        ty = sy+dy
        if tx < 0:
            tx = n + tx
        elif tx >= n:
            tx = tx % n
        if ty < 0:
            ty = m + ty
        elif ty >= m:
            ty = ty % m

        if l[tx][ty]!=0 and (tx,ty)!= w and (tx,ty)!=s:
            attack(l,(tx,ty),power//2)
            participated[(tx,ty)]=True
def probe(l):
    n=len(l)
    m=len(l[0])
    for i in range(n):
        for j in range(n):
            print(l[i][j], end=" ")
        print("")
    print("")

n,m,k=map(int,input().split())
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상
l=[list(map(int,input().split())) for i in range(n)]

attacked={}
initialize(attacked,l)

round=0

while True:
    participated={}

    round+=1

    #공격자의 좌표

    wx,wy=findWeakest(l,attacked)
    alive = countAlive(l)
    if alive<=1:
        break
    # 공격대상의 좌표
    sx, sy = findStrongest(l, attacked)
    participated[(wx,wy)]=True
    participated[(sx,sy)]=True
    l[wx][wy]+=(m+n)
    attacked[(wx,wy)]=round

    #나의 공격력
    power = l[wx][wy]

    #레이저 공격시도(우/하/좌/상)으로 우선순위 있음

    flag = laserAttack(l,participated,(wx,wy),(sx,sy),power)
    if not flag:
        shellAttack(l,participated,(wx,wy),(sx,sy),power)
    #포탑 정비
    cure(participated,l)


    if round==k:
        break


_max=0

for i in range(n):
    for j in range(m):
        if l[i][j]>_max:
            _max=l[i][j]
print(_max)