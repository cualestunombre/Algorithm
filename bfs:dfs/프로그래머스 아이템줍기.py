def solution(rectangle, characterX, characterY, itemX, itemY):
    inside = {}
    outline = {}
    adjacent = {}
    reg={}
    for i in rectangle:
        sx,sy,ex,ey=i
        if ex-sx==1 or ey-sy==1:
            reg[(sx,ex,sy,ey)]=True
        for j in range(sx,ex+1):
            for k in range(sy,ey+1):
                if j==sx or j== ex or k==sy or k==ey:
                    if (j,k) not in inside:
                        outline[(j,k)]=True
                else:
                    if (j,k) in outline:
                        del outline[(j,k)]
                    inside[(j,k)]=True
        for j in range(sx,ex+1):
            for k in range(sy,ey+1):
                if j == sx or j == ex or k == sy or k == ey:
                    if (j==sx and k==sy):
                        if (j,k) in adjacent:
                            adjacent[(j,k)]+=[(sx+1,sy),(sx,sy+1)]
                        else:
                            adjacent[(j, k)] = [(sx + 1, sy), (sx, sy + 1)]
                    elif (j==sx and k==ey):
                        if (j,k) in adjacent:
                            adjacent[(j,k)]+=[(sx,ey-1),(sx+1,ey)]
                        else:
                            adjacent[(j, k)] = [(sx, ey - 1), (sx + 1, ey)]
                    elif (j==ex and k ==sy):
                        if (j,k) in adjacent:
                            adjacent[(j,k)]+=[(ex-1,sy),(ex,sy+1)]
                        else:
                            adjacent[(j, k)] = [(ex - 1, sy), (ex, sy + 1)]
                    elif (j == ex and k == ey):
                        if (j,k) in adjacent:
                            adjacent[(j,k)]+=[(ex-1,ey),(ex,ey-1)]
                        else:
                            adjacent[(j, k)] = [(ex - 1, ey), (ex, ey - 1)]
                    elif (k==sy or k==ey):
                        if (j,k) in adjacent:
                            adjacent[(j,k)]+=[(j+1,k),(j-1,k)]
                        else:
                            adjacent[(j,k)]=[(j+1,k),(j-1,k)]
                    else:
                        if (j,k) in adjacent:
                            adjacent[(j,k)]+=[(j,k+1),(j,k-1)]
                        else:
                            adjacent[(j,k)]=[(j,k+1),(j,k-1)]

    for i in reg:
        sx,ex,sy,ey=i
        if ex-sx==1:# ex-sx ==1
            for j in range(sy+1,ey):
                if (sx,j) in outline and (sx+1,j) in outline:
                    if (sx+1,j) in adjacent[(sx,j)]:
                        adjacent[(sx,j)].remove((sx+1,j))
                    if (sx,j) in adjacent[(sx+1,j)]:
                        adjacent[(sx+1,j)].remove(((sx,j)))

        elif ey-sy==1:
            for j in range(sx+1,ex):
                if (j,sy) in outline and (j,sy+1) in outline:
                    if (j,sy+1) in adjacent[(j,sy)]:
                        adjacent[(j,sy)].remove((j,sy+1))
                    if (j,sy) in adjacent[(j,sy+1)]:
                        adjacent[(j,sy+1)].remove((j,sy))


    visited={}
    visited[(characterX,characterY)]=0
    q=[(characterX,characterY)]
    while q:
        x,y =q.pop(0)
        for dx,dy in adjacent[(x,y)]:
            if (dx,dy) in outline:
                if (dx,dy) not in visited:

                    visited[(dx,dy)]=visited[(x,y)]+1
                    q.append((dx,dy))
    answer = visited[(itemX,itemY)]
    return answer

print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]],1,4,6,3))