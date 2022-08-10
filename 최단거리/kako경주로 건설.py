import heapq
def dijkstra(start,end,board,dir):
    q=[(0,start,dir)] # 상 하 좌 우 각각 0 1 2 3
    expense={}
    n=end[0]+1
    for i in range(n):
        for j in range(n):
            expense[(i,j,0)]=7777777777
            expense[(i, j, 1)] = 7777777777
            expense[(i, j, 2)] = 7777777777
            expense[(i, j, 3)] = 7777777777
    expense[(start[0],start[1],dir)]=0
    while q:
        node=heapq.heappop(q)
        e,p,direction=node
        x,y=p # e는 거리 x ,y는 좌표
        if x+1<=n-1:
            if board[x+1][y]!=1:
                if direction!=1:
                    if e+600<=expense[(x+1,y,1)]:
                        heapq.heappush(q,(e+600,(x+1,y),1))
                        expense[(x+1,y,1)]=e+600
                else:
                    if e+100<=expense[(x+1,y,1)]:
                        heapq.heappush(q,(e+100,(x+1,y),1))
                        expense[(x+1,y,1)]=e+100
        if y+1<=n-1:
            if board[x][y+1]!=1:
                if direction!=3:
                    if e+600<=expense[(x,y+1,3)]:
                        heapq.heappush(q,(e+600,(x,y+1),3))
                        expense[(x,y+1,3)]=e+600
                else:
                    if e+100<=expense[(x,y+1,3)]:
                        heapq.heappush(q,(e+100,(x,y+1),3))
                        expense[(x,y+1,3)]=e+100
        if x-1>=0:
            if board[x-1][y]!=1:
                if direction!=0:
                    if e+600<=expense[(x-1,y,0)]:
                        heapq.heappush(q,(e+600,(x-1,y),0))
                        expense[(x-1,y,0)]=e+600
                else:
                    if e+100<=expense[(x-1,y,0)]:
                        heapq.heappush(q,(e+100,(x-1,y),0))
                        expense[(x-1,y,0)]=e+100
        if y-1>=0:
            if board[x][y-1]!=1:
                if direction!=2:
                    if e+600<=expense[(x,y-1,2)]:
                        heapq.heappush(q,(e+600,(x,y-1),2))
                        expense[(x,y-1,2)]=e+600
                else:
                    if e+100<=expense[(x,y-1,2)]:
                        heapq.heappush(q,(e+100,(x,y-1),2))
                        expense[(x,y-1,2)]=e+100
    l=[expense[(end[0],end[1],i)] for i in range(0,4)]
    l.sort()
    return l[0]





def solution(board):
    n=len(board)-1
    answer = min(dijkstra((0,0),(n,n),board,1),dijkstra((0,0),(n,n),board,3))
    return answer