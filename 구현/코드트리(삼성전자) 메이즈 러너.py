global move
move = 0
n,m,k = map(int,input().split())
l = [list(map(int,input().split())) for i in range(n)]
pos = [tuple(map(int,input().split())) for i in range(m)]

ex,ey = map(int,input().split())

# 빈칸 0 벽 1-9의 내구도, 회전할 때 내구도 1씩 깎임, 내구도 0 시 빈 칸
# 참가자는 상하좌우로 움직일 수 있음 움직인 칸은 출구까지의 최단 거리가 더 가까워야 함, 움직일 수 없으면 움직이지 않음, 상하가 우선순위
# 이동을 끝내면 미로가 회전함
# 출구와 참가자를 포함한 가장 작은 정사각형을 잡음, 선택된 정사각형은 시계방향 90도 회전함, 회전한 벽은 내구도 1 감소
DIR = [(1,0),(-1,0),(0,1),(0,-1)]

def canGo(x,y):
    n = len(l)
    if x>=1 and x<=n and y>=1 and y<=n and l[x-1][y-1] == 0: #움직일 수 있으면
        return True
    return False

def calDistance(x,y,cx,cy):
    return abs(x-cx) + abs(y-cy)

def playersMove(ex,ey):
    global move
    toMove = []
    for x,y in pos:
        arr = []
        for index,dot in enumerate(DIR):
            dx,dy = dot
            distance = calDistance(x+dx,y+dy,ex,ey)
            comp = calDistance(x,y,ex,ey)
            if canGo(x+dx,y+dy) and distance<comp: #원래의 거리(comp)보다 작으면
                arr.append((x+dx,y+dy,index))
        arr.sort(key=lambda x:x[2])
        if arr:
            if (ex,ey) == (arr[0][0],arr[0][1]):
                pass
            else:
                toMove.append((arr[0][0],arr[0][1]))
            move += 1
        else:
            toMove.append((x,y))
    return toMove

def makeRectangle(ex,ey):
    arr = []
    n = len(l)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i+k>=n or j+k>=n:
                    break
                if ex>=i+1 and ey>=j+1 and ex<=i+1+k and ey<=j+1+k:
                    pass
                else:
                    continue
                flag = False
                for x,y in pos:
                    if x>=i+1 and y>=j+1 and x<=i+1+k and y<=j+1+k:
                        flag = True
                        break
                if flag:
                    arr.append((i+1,j+1,k+1))



    return arr

def clockWiseRotate(x,y,size,ex,ey):
    temp = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            temp[i][j] = l[x+size-2-j][y+i-1] #실좌표


    for i in range(size):
        flag = False
        for j in range(size):
            if (x+size-1-j,y+i) == (ex,ey): # 짭 좌표
                ex,ey = (x+i,y+j)

                flag = True
                break
        if flag:
            break

    for p in range(len(pos)):
        for i in range(size):
            flag = False
            for j in range(size):
                if (x+size-1-i,y+j) == pos[p]:
                    pos[p] = (x+j,y+i)
                    flag = True
                    break
            if flag:
                break

    for i in range(size):
        for j in range(size):
            if temp[i][j] != 0:
                temp[i][j] -= 1
            l[x+i-1][y+j-1] = temp[i][j]

    return ex,ey

turn = 0
while turn<k:

    pos = playersMove(ex,ey)
    if not pos:
        break
    ret = makeRectangle(ex,ey)
    ret.sort(key=lambda x:(x[2],x[0],x[1])) # x좌표 y좌표 크기
    ex,ey = clockWiseRotate(ret[0][0],ret[0][1],ret[0][2],ex,ey)


    turn += 1

print(move)
print(ex,ey)








