global ox,oy,minimum
minimum = 10**100
n,m = map(int,input().split())
l = [list(input()) for i in range(n)]
def handleEnd(rx,ry,bx,by,nrx,nry,nbx,nby):
    global ox,oy
    l[nrx][nry], l[nbx][nby] = '.', '.'
    l[rx][ry], l[bx][by] = 'R', 'B'
    l[ox][oy] = 'O'
DIR = [(-1,0),(0,1),(1,0),(0,-1)]
def handleMove(arg,direction):
    global ox,oy
    x,y,tp = arg
    cx,cy = x,y
    dx,dy = DIR[direction]
    while True:
        cx+=dx
        cy+=dy
        if l[cx][cy] == "#" or l[cx][cy] == "B" or l[cx][cy] == "R":
            cx-=dx
            cy-=dy
            break
        elif l[cx][cy] == ".":
            continue
        elif l[cx][cy] == "O":
            break
    if (x,y) == (cx,cy): #이동해도 못가면
        return x,y,tp
    elif l[cx][cy] == 'O':
        l[x][y] = '.'
        return cx,cy,tp
    else: #조금이라도 움직임
        l[x][y] = '.'
        l[cx][cy] = tp
        return cx,cy,tp






def move(rx,ry,bx,by,direction):
    cand = [(rx,ry,'R'),(bx,by,'B')]
    if direction == 0:
        cand.sort(key=lambda x:x[0])
    if direction == 1:
        cand.sort(key=lambda x:-x[1])
    if direction == 2:
        cand.sort(key=lambda x:-x[0])
    if direction == 3:
        cand.sort(key=lambda x:x[1])
    fx,fy,ft = handleMove(cand[0],direction)
    sx,sy,st = handleMove(cand[1],direction)

    if ft == 'R':
        return fx,fy,sx,sy
    else:
        return sx,sy,fx,fy
def probe():
    n,m = len(l), len(l[0])
    for i in range(n):
        for j in range(m):
            print(l[i][j],end=" ")
        print("")
    print("")

def doTheWork(step,direction,rx,ry,bx,by):
    global ox,oy,minimum
    if step == 10:
        return
    #새로 이동한 좌표


    nrx,nry,nbx,nby = move(rx,ry,bx,by,direction)


    if (nbx,nby) == (ox,oy):
        handleEnd(rx,ry,bx,by,nrx,nry,nbx,nby)
        return
    elif (nrx,nry) == (ox,oy):
        handleEnd(rx, ry, bx, by, nrx, nry, nbx, nby)
        minimum = min(minimum,step+1)
        return


    for i in range(4):
        doTheWork(step+1,i,nrx,nry,nbx,nby)
    handleEnd(rx, ry, bx, by, nrx, nry, nbx, nby)

    return






rx,ry,bx,by = 0,0,0,0
for i in range(n):
    for j in range(m):
        if l[i][j] == 'R':
            rx,ry = i,j
        if l[i][j] == 'B':
            bx,by = i,j
        if l[i][j] == 'O':
            ox,oy = i,j

#0북 1동 2남 3서

doTheWork(0,0,rx,ry,bx,by)

doTheWork(0,1,rx,ry,bx,by)

doTheWork(0,2,rx,ry,bx,by)

doTheWork(0,3,rx,ry,bx,by)

if minimum == 10**100:
    print(-1)
else:
    print(minimum)