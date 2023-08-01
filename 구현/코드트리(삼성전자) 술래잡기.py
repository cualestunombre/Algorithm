n,m,h,k = map(int,input().split()) # n크기, m 도망자, h 나무, k턴
deserters = {}
trees = {}
cache = []
#체포조의 좌표
dpx , dpy,dpd = n//2+1,n//2+1,3
DIR = [(0,1),(1,0),(0,-1),(-1,0)]

#d 0우, 1하, 2좌 3상
def convertDir(d):
    return (d + 2) % 4
def clockWise(d):
    return (d + 1) % 4
def counter(d):
    return (d + 3) % 4
def cacheInit(n,cache):
    cache.append((3,3,3))
    # x,y,d
    sx,sy,sd = n//2+1,n//2+1,3
    step = 1
    count = 0
    while True:
        dx,dy = DIR[sd]
        ######
        if sx+dx<=0 or sx+dx>n or sy+dy>n or sy+dy<=0:
            cache.pop(),cache.pop()
            break
        ######
        for i in range(1,step+1):
            if i == step:
                mx, my = dx , dy
                cache.append((sx + mx, sy + my,clockWise(sd)))
                sx, sy, sd = sx + dx, sy + dy, clockWise(sd)
            else:
                mx, my = dx , dy
                cache.append((sx+mx,sy+my,sd))
                sx, sy, sd = sx + dx, sy + dy, sd
        count+=1
        if count == 2:
            count = 0
            step+=1
    bucket = [(1,1,1)]
    #i번째는 23-i의 방향과 24-i의 좌표를 가져온다
    for i in range(1,len(cache)):
        d = cache[23-i][2]
        x,y = cache[24-i][0],cache[24-i][1]
        bucket.append((x,y,convertDir(d)))
    for i in bucket:
        cache.append(i)









for i in range(m): #d 0우, 1하, 2좌 3상
    x,y,d = map(int,input().split())
    if (x,y) in deserters:
        deserters[(x,y)].append(d-1)
    else:
        deserters[(x,y)]=[d-1]

for i in range(h):
    x,y = map(int,input().split())
    trees[(x,y)] = True


# 1 1 1 2 2 3 3 4 4 4
turn = 0
score = 0
cacheInit(n,cache)


while turn < k:

    #체포조와 거리가 3이하인 탈영병 움직이기
    desertersMove = {}
    for x,y in deserters:
        #거리가 3 이하
        if abs(dpx-x) + abs(dpy-y) <= 3:
            for d in deserters[(x,y)]:
                dx,dy = DIR[d]
                #격자를 안벗어나면
                if dx+x>0 and dx+x <= n and dy+y>0 and dy+y <= n:

                    if (dx+x,dy+y) != (dpx,dpy):
                        if (dx+x,dy+y) not in desertersMove:
                            desertersMove[(dx+x,dy+y)] = [d]
                        else:
                            desertersMove[(dx+x,dy+y)].append(d)
                    else:
                        if (x,y) not in desertersMove:
                            desertersMove[(x,y)] = [d]
                        else:
                            desertersMove[(x,y)].append(d)

                #격자를 벗어나면
                elif dx+x<=0 or dx+x > n or dy+y <=0 or dy+y >n:
                    nd = convertDir(d)
                    dx,dy = DIR[nd]

                    if (dx+x,dy+y) != (dpx,dpy):
                        if (dx+x,dy+y) not in desertersMove:
                            desertersMove[(dx+x,dy+y)] = [nd]
                        else:
                            desertersMove[(dx+x,dy+y)].append(nd)
                    else:
                        if (x,y) not in desertersMove:
                            desertersMove[(x,y)] = [nd]
                        else:
                            desertersMove[(x,y)].append(nd)

        #거리가 3 이상
        else:
            for d in deserters[(x,y)]:
                if (x,y) not in desertersMove:
                    desertersMove[(x,y)] = [d]
                else:
                    desertersMove[(x,y)].append(d)

    deserters = desertersMove
    # d 0우, 1하, 2좌 3상
    dpx,dpy,dpd = cache[(turn+1)%(n**2*2-2)]

    dx, dy = DIR[dpd]
    add = 0


    for i in range(3):
        tx,ty = dpx + (i)*dx, dpy + (i)*dy
        if (tx,ty) not in trees and tx>0 and tx<=n and ty>0 and ty<=n:
            if (tx,ty) in deserters:
                add += len(deserters[(tx,ty)])
                del deserters[(tx,ty)]


    score += add*(turn+1)
    turn += 1

print(score)





