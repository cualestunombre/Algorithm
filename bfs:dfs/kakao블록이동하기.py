from collections import deque
def func(dx,dy,cx,cy,board):
    n=len(board)
    dir=[(0,-1),(0,1),(1,0),(-1,0)]
    cand=[]
    #평행이동
    for x,y in dir:
        if dx+x>=0 and dx+x<n and dy+y>=0 and dy+y<n and cx+x>=0 and cx+x<n and cy+y>=0 and cy+y<n:
            if board[dx+x][dy+y]!=1 and board[cx+x][cy+y]!=1:
                cand.append((dx+x,dy+y,cx+x,cy+y))
    #가로회전
    if dx==cx:
        if dy>cy:
            px,py,qx,qy = cx,cy,dx,dy
        else:
            px,py,qx,qy = dx,dy,cx,cy
        # px축으로 반시계회전
        if qx-1>=0 and board[qx-1][qy]==0 and board[qx-1][qy-1]==0:
            cand.append((px,py,qx-1,qy-1))
        # px축으로 시계회전
        if qx+1<n and board[qx+1][qy]==0 and board[qx+1][qy-1]==0:
            cand.append((px,py,qx+1,qy-1))
        # qx축으로 시계회전
        if px-1>=0 and board[px-1][py+1]==0 and board[px-1][py]==0:
            cand.append((px-1,py+1,qx,qy))
        # qx축으로 반시계회전
        if px+1<n and board[px+1][py]==0 and board[px+1][py+1]==0:
            cand.append((px+1,py+1,qx,qy))
    #세로회전
    if dy==cy:
        if dx>cx:
           px,py,qx,qy = cx,cy,dx,dy
        else:
            px,py,qx,qy = dx,dy,cx,cy
        #px축으로 반시계회전
        if qy+1<n and board[qx][qy+1]==0 and board[qx-1][qy+1]==0:
            cand.append((px,py,qx-1,qy+1))
        #px축으로 시계회전
        if qy-1>=0 and board[qx][qy-1]==0 and board[qx-1][qy-1]==0:
            cand.append((px,py,qx-1,qy-1))
        #qx축으로 시계회전
        if py+1<n and board[px][py+1]==0 and board[px+1][py+1]==0:
            cand.append((px+1,py+1,qx,qy))
        #qx축으로 반시계회전
        if py-1>=0 and board[px][py-1]==0 and board[px+1][py-1]==0:
            cand.append((px+1,py-1,qx,qy))
    return cand


def solution(board):
    n=len(board)
    visited={}
    visited[(0,0,0,1)]=True
    visited[(0,1,0,0)]=True
    q=deque([(0,0,0,1,0)])
    while q:
        dx,dy,cx,cy,count=q.popleft()
        cand = func(dx,dy,cx,cy,board)
        for a,b,c,d in cand:
            if (a,b,c,d) not in visited and (c,d,a,b) not in visited:
                visited[(a,b,c,d)]=True
                visited[(c,d,a,b)]=True
                if (a==n-1 and b==n-1) or (c==n-1 and d==n-1):
                    return count+1
                q.append((a,b,c,d,count+1))

solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]])