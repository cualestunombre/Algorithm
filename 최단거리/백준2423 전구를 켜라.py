import heapq
def check(x,y,n,m):
    if (x,y) == (n,m):
        return True
    if x>=0 and x<n and y>=0 and y<m:
        return True
DIR = {'\\':[(1,0),(1,1),(0,1),(-1,-1),(-1,0),(0,-1)],'/':[(-1,0),(0,1),(-1,1),(1,0),(1,-1),(0,-1)]}
dic = {("/",-1,0,"/"):(1,"\\"),("/",-1,0,"\\"):(0,"\\"),
       ("/",-1,1,"/"):(0,"/"),("/",-1,1,"\\"):(1,"/"),
       ("/",0,1,"/"):(1,"\\"),("/",0,1,"\\"):(0,"\\"),
       ("/",1,0,"/"):(1,"\\"),("/",1,0,"\\"):(0,"\\"),
       ("/",1,-1,"/"):(0,"/"),("/",1,-1,"\\"):(1,"/"),
       ("/",0,-1,"/"):(1,"\\"),("/",0,-1,"\\"):(0,"\\"),
       ("\\",0,1,"/"):(0,"/"),("\\",0,1,"\\"):(1,"/"),
       ("\\",1,1,"\\"):(0,"\\"),("\\",1,1,"/"):(1,"\\"),
       ("\\",1,0,"/"):(0,"/"),("\\",1,0,"\\"):(1,"/"),
       ("\\",-1,-1,"\\"):(0,"\\"),("\\",-1,-1,"/"):(1,"\\"),
       ("\\",-1,0,"/"):(0,"/"),("\\",-1,0,"\\"):(1,"/"),
       ("\\",0,-1,"/"):(0,"/"),("\\",0,-1,"\\"):(1,"/")
       }
n,m = map(int,input().split())
l = [input() for i in range(n)]
l.append("".join(["\\" for _ in range(m+1)]))
visited = {}
if l[0][0] == '/':
    visited[(0,0)] = 1
else:
    visited[(0,0)] = 0
q = [(visited[0,0],0,0,"\\")]
while q:
    rotate,x,y,direction = heapq.heappop(q)
    if rotate > visited[(x,y)]:
        continue
    for dx,dy in DIR[direction]:
        if check(x+dx,y+dy,n,m):
            nextRotate,nextDir = dic[(direction,dx,dy,l[x+dx][y+dy])]
            if (x+dx,y+dy) not in visited:
                visited[(x+dx,y+dy)] = rotate + nextRotate
                heapq.heappush(q,(rotate+nextRotate,x+dx,y+dy,nextDir))
            else:
                comp = visited[(x+dx,y+dy)]
                if comp > rotate + nextRotate:
                    visited[(x + dx, y + dy)] = rotate + nextRotate
                    heapq.heappush(q, (rotate + nextRotate, x + dx, y + dy,nextDir))
if (n,m) not in visited:
    print("NO SOLUTION")
else:
    print(visited[(n,m)])






