from collections import deque
import copy
global minimum
global cnt
minimum=10000000000000


def cal(cur,f,s,board):
    return implCal(cur,f,board)+implCal(f,s,board)+2
def implCal(s,e,board):
    q=deque()
    q.append(s)
    visited={s:0}
    dir=[(0,-1),(1,0),(-1,0),(0,1)]
    while q:
        x,y = q.popleft()
        if e in visited:
            break
        for dx,dy in dir:
            curx, cury = (x, y)
            change=0
            while True:
                if curx+dx>=0 and curx+dx<4 and cury+dy>=0 and cury+dy<4:
                    curx+=dx
                    cury+=dy
                    change+=1
                    if(curx,cury) not in visited:
                        if board[curx][cury]!=0:
                            q.append((curx,cury))
                            visited[(curx,cury)]=1+visited[(x,y)]
                            break
                        if change==1:
                            q.append((curx,cury))
                            visited[(curx,cury)]=1+visited[(x,y)]
                            continue
                        if curx+dx<0 or curx+dx>=4 or cury+dy<0 or cury+dy>=4:
                            q.append((curx,cury))
                            visited[(curx,cury)]=1+visited[(x,y)]
                            break
                else:
                    break
    return visited[e]




def brute(target,visited,board,cur,value,dic):
    global cnt
    global minimum
    print(visited)
    visited.append(target)
    x,y=dic[target][0]
    dx,dy=dic[target][1]
    distFirst = cal(cur,(x,y), (dx,dy), board)
    distSecond = cal(cur,(dx,dy), (x,y), board)

    if len(visited) >= cnt:
        if minimum > min(distFirst,distSecond)+value:
            minimum = min(distFirst,distSecond)+value
        visited.pop()
        return

    #(x,y)->(dx,dy)
    board[x][y]=0
    board[dx][dy]=0
    for i in range(1,7):
        if i in dic and i not in visited:
            brute(i,visited,board,(dx,dy),value+distFirst,dic)
            brute(i, visited, board, (x, y), value + distSecond, dic)
    # (dx,dy)->(x,y)
    visited.pop()
    board[x][y]=target
    board[dx][dy]=target
    return





def solution(board, r, c):
    global minimum
    global cnt
    dic={}
    for i in range(4):
        for j in range(4):
            value=board[i][j]
            if value not in dic:
                dic[value]=[(i,j)]
            else:
                dic[value].append((i,j))
    cnt=len(dic.keys())-1
    l=[]
    for i in range(1,7):
        if i in dic:
            brute(i,l,board,(r,c),0,dic)

    return minimum

print(solution([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]],0,0))