global check
global endTurn
check=False

dir=[(0,-1),(0,1),(1,0),(-1,0),(1,-1),(-1,1),(-1,-1),(1,1),(0,0)]

def wallCal(i,j,turn):
    if (i-turn+1,j) in wall:
        return False
    return True
def dfs():
    global check
    global endTurn
    stack=[(7,0,1)]
    visited[(7,0,1)]=True
    while stack:
        x,y,z = stack.pop()
        if endTurn <=z or (x==0 and y==7):
            check=True
            return
        for dx,dy in dir:
            if (x+dx>=0 and x+dx<=7 and y+dy>=0 and y+dy<=7) and wallCal(x+dx,y+dy,z+1) and (x+dx,y+dy,z+1) not in visited and wallCal(x+dx,y+dy,z):
                visited[(x+dx,y+dy,z+1)]=True

                stack.append((x+dx,y+dy,z+1))







endTurn=0
l=[input() for i in range(8)]
wall={}
for i in range(8):
    for j in range(8):
        if l[i][j]=='#':
            wall[(i,j)]=True
for i in range(8):
    switch=True
    for j in range(8):
        if l[i][j]=='#':
            endTurn=9-i
            switch=False
            break
    if switch==False:
        break
visited={}
dfs()
if check:
    print(1)
else:
    print(0)

