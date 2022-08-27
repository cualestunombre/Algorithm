r,c,k = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(r)] #초기 정보
n = int(input())
walls = [tuple(map(int,input().split())) for i in range(n)]#벽 정보
dicWall ={}
mpos = {} # 온풍기 정보
shouldCheck ={} # 확인해야할 곳 정보
for i in range(r):
    for j in range(c):
        dicWall[(i,j)]=[]
for x,y,t in walls:
    if t==0:
        dicWall[(x-1,y-1)]+=[(x-2,y-1)]
        dicWall[(x-2,y-1)]+=[(x-1,y-1)]
    else:
        dicWall[(x-1,y-1)]+=[(x-1,y)]
        dicWall[(x-1,y)]+=[(x-1,y-1)]


temp = [[0 for i in range(c)] for j in range(r)]
def check(r,c,x,y):
    if x<=r-1 and x>=0 and y<=c-1 and y>=0:
        return True
    else:
        return False

for i in range(r):
    for j in range(c):
        if l[i][j]>=1 and l[i][j]<=4:
            mpos[(i,j)]=l[i][j]
        elif l[i][j]==5:
            shouldCheck[(i,j)]=True
time = 0
switch=False
while True:
    time+=1
    for x,y in mpos:
        if mpos[(x,y)]==1: #오른쪽
            f=0
            s=1
            fs=1
            ss=1
            ds=1
            gs=0
            hs=-1
            xs=1
            rs=-1
            ts=0
        if mpos[(x,y)]==2: #왼쪽
            f=0
            s=-1
            fs=-1
            ss=-1
            ds=-1
            gs=0
            hs=1
            xs=-1
            rs=1
            ts=0
        if mpos[(x,y)]==3: #위
            f=-1
            s=0
            fs=-1
            ss=-1
            ds=0
            gs=-1
            hs=-1
            xs=1
            rs=0
            ts=1
        if mpos[(x,y)]==4: #아래
            f=1
            s=0
            fs=1
            ss=1
            ds=0
            gs=1
            hs=1
            xs=-1
            rs=0
            ts=-1
        visited = {(x + f, y + s): True}
        q = [(x + f, y + s, 5)]
        while q:
            sx,sy,score =q.pop(0)
            temp[sx][sy]+=score
            if check(r,c,sx+f,sy+s) and score>1 and (sx+f,sy+s) not in visited:
                if (sx+f,sy+s) not in dicWall[(sx,sy)]:
                    q.append((sx + f, sy + s, score - 1))
                    visited[(sx + f, sy + s)] = True
            if check(r,c,sx+fs,sy+ss) and score>1 and (sx+fs,sy+ss) not in visited:
                if (sx+ds,sy+gs) not in dicWall[(sx,sy)] and (sx+fs,sy+ss) not in dicWall[(sx+ds,sy+gs)]:
                    q.append((sx + fs, sy + ss, score - 1))
                    visited[(sx + fs, sy + ss)] = True
            if check(r,c,sx+hs,sy+xs) and score>1 and (sx+hs,sy+xs) not in visited:
                if (sx+rs,sy+ts) not in dicWall[(sx,sy)] and (sx+hs,sy+xs) not in dicWall[(sx+rs,sy+ts)]:
                    q.append((sx + hs, sy + xs, score - 1))
                    visited[(sx + hs, sy + xs)] = True
    to_add={}
    dir=[(0,-1),(1,0),(0,1),(-1,0)]
    for i in range(r):
        for j in range(c):
            for ax,ay in dir:
                if i+ax>=0 and i+ax<r and j+ay<c and j+ay>=0:
                    if (i,j) in dicWall:
                         if (i+ax,j+ay) not in dicWall[(i,j)]:
                             if (i,j) not in to_add:
                                 to_add[(i,j)]=-int((temp[i][j]-temp[i+ax][j+ay])/4)
                             else:
                                 to_add[(i, j)] -= int((temp[i][j] - temp[i + ax][j + ay]) / 4)
                    else:
                        if (i, j) not in to_add:
                            to_add[(i, j)] = -int((temp[i][j] - temp[i + ax][j + ay]) / 4)
                        else:
                            to_add[(i, j)] -= int((temp[i][j] - temp[i + ax][j + ay]) / 4)

    for i,j in to_add:
         temp[i][j]+=to_add[(i,j)]
    for i in range(r):
        for j in range(c):
            if i==0 or i==r-1:
                if temp[i][j]-1>=0:
                    temp[i][j]-=1
            else:
                if j==0 or j==c-1:
                    if temp[i][j]-1>=0:
                        temp[i][j]-=1

    switch2=True
    for i,j in shouldCheck:
        if temp[i][j]<k:
            switch2=False
    if switch2==True:
        switch=True
        break
    if time>100:
        break

if switch==True:
    print(time)
else:
    print(101)













