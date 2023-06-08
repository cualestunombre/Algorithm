import heapq

class StaticClass:
    n,m = 0,0
    DIR = [(0,-1),(0,1),(1,0),(-1,0)]


def convertHelper(x, standard):
    if 0 <= x < standard:
        return x
    tx = abs(x) - standard
    quotient = tx // (standard - 1)
    remainder = tx % (standard - 1)
    if quotient == 0 or quotient % 2 == 0:
        return standard - 2 - remainder
    else:
        return remainder + 1


def convert(x,y):
    rx,ry = convertHelper(x,StaticClass.n) , convertHelper(y,StaticClass.m)
    return (rx,ry)


def getTarget(pid,rabbits):
    bucket = []
    curx,cury = rabbits[pid][1]
    distance = rabbits[pid][0]
    for dx,dy in StaticClass.DIR:
        sx,sy = dx*distance, dy*distance
        nx , ny = curx+sx , cury+sy
        bucket.append(convert(nx,ny))
    bucket.sort(key=lambda x:(-(x[0]+x[1]),-x[0],-x[1]))
    return bucket[0]

def init(ret,rabbits):
    while ret:
        d, pid  = ret.pop(), ret.pop()
        rabbits[pid] = [d,(0,0),0,0]

def startGame(k,s,rabbits):
    SDG = {}  # selectedDuringGame
    q = []
    for rabbit in rabbits:
        heapq.heappush(q,(rabbits[rabbit][3],rabbits[rabbit][1][0]+rabbits[rabbit][1][1],rabbits[rabbit][1][0],rabbits[rabbit][1][1],rabbit))
    for count in range(k):
        winner = heapq.heappop(q)
        winner = winner[4]
        SDG[winner]=True
        rabbits[winner][3]+=1

        target = getTarget(winner,rabbits)
        rabbits[winner][1]=target
        for rabbit in rabbits:
            if rabbit != winner:
                rabbits[rabbit][2] += (target[0] + target[1] + 2)

        heapq.heappush(q,(rabbits[winner][3],rabbits[winner][1][0]+rabbits[winner][1][1],rabbits[winner][1][0],rabbits[winner][1][1],winner))



    bucket = []
    for rabbit in SDG:
        bucket.append((rabbits[rabbit][1][0],rabbits[rabbit][1][1],rabbit))
    bucket.sort( key=lambda x:(-(x[0]+x[1]),-x[0],-x[1],-x[2]) )
    winner = bucket[0][2]
    rabbits[winner][2] += s




if __name__ == "__main__":
    q = int(input())
    ret = list(map(int, input().split()))
    ret.pop(0)
    n,m,p = ret.pop(0),ret.pop(0),ret.pop(0)
    StaticClass.n , StaticClass.m = n,m

    #토끼의 pid를 키로하여, 이동거리 정보와 좌표를 담은 딕셔너리
    rabbits = {}
    init(ret,rabbits)


    for i in range(q-2):
        ret = list(map(int,input().split()))
        if ret[0] == 200:
            startGame(ret[1],ret[2],rabbits) #K,S를 인자로 함
        if ret[0] == 300:
            pid, l = ret[1], ret[2]
            rabbits[pid][0] *= ret[2]
    terminate = int(input())

    _max = 0
    for rabbit in rabbits:
        if rabbits[rabbit][2]>_max:
            _max = rabbits[rabbit][2]
    print(_max)
