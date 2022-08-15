# 자기보다 큰 물고기칸은 지나갈 수 없고 먹을 수도 없다
# 자기랑 크기가 같으면 먹을 수는 없고 지나갈 수는 있다
# 자기보다 작으면 먹을 수도 있고 지나갈 수도 있다
dir=[(0,-1),(0,1),(1,0),(-1,0)]
n = int(input())
l=[list(map(int,input().split())) for i in range(n)]
size=2
ate=0
time=0
for i in range(n):
    for j in range(n):
        if l[i][j]==9:
            curPos = [i,j]
while True:
    toEat = []
    visited={(curPos[0],curPos[1]):0}
    q=[(curPos[0],curPos[1])]
    while q:
        x,y=q.pop(0)
        for dx,dy in dir:
            if x+dx>=0 and x+dx<=n-1 and y+dy>=0 and y+dy<=n-1:
                if (dx+x,dy+y) not in visited and l[dx+x][dy+y]<=size:
                    visited[(dx+x,dy+y)]=visited[(x,y)]+1
                    q.append((dx+x,dy+y))
                    if l[dx+x][dy+y]<size and l[dx+x][dy+y]!=0:
                        dist=visited[(x,y)]+1
                        toEat.append((l[dx+x][dy+y],dist,dx+x,dy+y))
    if not toEat:
        break
    toEat.sort(key=lambda x:(x[1],x[2],x[3]))
    l[curPos[0]][curPos[1]]=0
    curPos[0]=toEat[0][2]
    curPos[1]=toEat[0][3]
    l[curPos[0]][curPos[1]] = 0
    time+=toEat[0][1]
    ate+=1
    if ate==size:
        size+=1
        ate=0

print(time)

