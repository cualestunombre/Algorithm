global maximum,m,n
import sys
sys.setrecursionlimit(100000)
maximum = 0
DIR = [(-1,0),(0,1),(1,0),(0,-1)]
cache = {}
def check(x,y):
    global m,n
    if x>=0 and x<n and y>=0 and y<m and l[x][y]!='H':
        return True
    return False

def dp(x,y,direction,called):
    if called>=10000:
        return 10000
    if (x,y,direction) in cache:
        return cache[(x,y,direction)]
    dx,dy = DIR[direction]
    number = int(l[x][y])
    nx,ny = dx*number,dy*number
    if not check(nx+x,ny+y):
        cache[(x,y,direction)] = 1
        return 1
    ret = 0
    for i in range(4):
        ret = max(ret,dp(nx+x,ny+y,i,called+1))
    cache[(x,y,direction)] = ret + 1
    return ret + 1


n,m = map(int,input().split())
l = [input() for i in range(n)]
cache = {}



value = max(max(dp(0, 0, 0,0), dp(0, 0, 1,0)), max(dp(0, 0, 2,0), dp(0, 0, 3,0)))
if value>=10000:
    print(-1)
else:
    print(value)