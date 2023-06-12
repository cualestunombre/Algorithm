n,m = map(int,input().split())
x,y,d = map(int,input().split())
l = [list(map(int,input().split())) for i in range(n)]
visited ={(x,y):True}
DIR = [(-1,0),(0,1),(1,0),(0,-1)]
count = 1

def valid(x,y,n,m):
    if x>=0 and x<n and y>=0 and y<m and (x,y) not in visited and l[x][y]!=1:
        return True
    return False

def makeLeft(x, y, d):
    dx, dy = DIR[(d + 3) % 4]
    return (x + dx, y + dy, (d + 3) % 4)

def moveBack(x,y,curd):
    dx,dy = DIR[curd]
    dx,dy = -dx,-dy
    return (dx+x,dy+y)

#0,1,2,3 순서대로 북 동 남 서
# 0도로 1인도
curx,cury,curd = x,y,d
while True:

    nextx,nexty,curd = makeLeft(curx,cury,curd)
    if valid(nextx,nexty,n,m):
        curx,cury = nextx,nexty
        visited[(curx,cury)]=True
        count+=1
    else:
        flag = False
        for i in range(3):
            nextx,nexty,curd = makeLeft(curx,cury,curd)
            if valid(nextx,nexty,n,m):
                curx,cury= nextx,nexty
                visited[(curx,cury)]=True
                count += 1
                flag=True
                break
        if not flag:
            curx,cury = moveBack(curx,cury,curd)
            if curx<0 or curx>=n or cury<0 or cury>=m or l[curx][cury]==1:
                break
            visited[(curx,cury)]=True
            count += 1
print(len(visited))
