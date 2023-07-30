m,t = map(int,input().split())
r,c = map(int,input().split())
DIR = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
moveDir = [(-1,0),(0,-1),(1,0),(0,1)]
monsters = {}
deadBodies = {}
time = 0

def movePackMan(l,pack,monsters):
    answer = 0
    px,py = pack
    visited = {}
    for index in l:
        dx,dy = moveDir[index]
        if px+dx>0 and px+dx<=4 and py+dy>0 and py+dy<=4:
            px +=dx
            py +=dy
            answer = len(monsters[(px,py)]) +answer  if (px,py) in monsters and (px,py) not in visited else answer
            visited[(px,py)] = True
        else:
            return 0
    return answer


def moveMonster(cur, pack, d, deadBodies, toMove):
    x,y = cur
    px,py = pack

    for i in range(8):
        di = (d+i) % 8
        dx,dy = DIR[di]
        if dx+x>0 and dx+x<=4 and dy+y>0 and dy+y<=4 and (x+dx,y+dy) not in deadBodies and (dx+x,dy+y) != (px,py):
            if (dx+x,dy+y) in toMove:
                toMove[(dx+x,dy+y)].append(di)
            else:
                toMove[(dx+x,dy+y)]=[di]
            return


    if (x,y) in toMove:
        toMove[(x, y)].append(d)
    else:
        toMove[(x,  y)] = [d]
    return


def makeCand():
    answer = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                answer.append([i,j,k])
    return answer

def killMonsters(pack,bucket,monsters,deadBodies):
    r,c = pack
    for i in range(1,len(bucket)):
        dx,dy = moveDir[bucket[i]]
        r+=dx
        c+=dy
        if (r,c) in monsters:
            if (r,c) in deadBodies:
                deadBodies[(r,c)][2] = True
            else:
                deadBodies[(r,c)] = {2:True}
            del monsters[(r,c)]
    return r,c


for i in range(m):
    x,y,d = map(int,input().split())
    if (x,y) in monsters:
        monsters[(x,y)].append(d-1)
    else:
        monsters[(x,y)] = [d-1]

curr,curc = r,c
while time < t:
    #복제시도
    eggs = {}
    for x,y in monsters:
        for d in monsters[(x,y)]:
            if (x,y) not in eggs:
                eggs[(x,y)]=[d]
            else:
                eggs[(x,y)].append(d)

    #몬스터 이동
    toMove = {}
    for x,y in monsters:
        for d in monsters[(x,y)]:
            moveMonster((x,y),(curr,curc),d,deadBodies,toMove)
    monsters = toMove
    toMove = {}


    #팩맨이동 0상 1좌 2하 3우
    cand = makeCand()
    bucket = [[movePackMan(i,(curr,curc),monsters)]+i for i in cand]
    bucket.sort(key=lambda x:(-x[0],x[1],x[2],x[3]))
    curr,curc = killMonsters((curr,curc),bucket[0],monsters,deadBodies)

    #0상, 1좌, 2하, 3우


    #몬스터 시체 소멸
    toDel = {}
    for x,y in deadBodies:
        if 0 in deadBodies[(x,y)]:
            del deadBodies[(x,y)][0]
        if 1 in deadBodies[(x,y)]:
            del deadBodies[(x,y)][1]
            deadBodies[(x,y)][0] = True
        if 2 in deadBodies[(x,y)]:
            del deadBodies[(x,y)][2]
            deadBodies[(x,y)][1] = True
        if 1 not in deadBodies[(x,y)] and 0 not in deadBodies[(x,y)]:
            toDel[(x,y)] = True

    for i in toDel:
        del deadBodies[i]



    for x,y in eggs:
        for d in eggs[(x,y)]:
            if (x,y) in monsters:
                monsters[(x,y)].append(d)
            else:
                monsters[(x,y)]=[d]


    time+=1

count = 0
for i in monsters:
    for d in monsters[i]:
        count += 1



print(count)
#좌표 별로 리스트를 관리하기

