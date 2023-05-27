from collections import deque as dq
global teamNo #팀을 구별하기 위한 전역 변수

teamNo=0
score=0

n,m,k = map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
#입출력


team={} #팀의 정보를 담은 딕셔너리
teamMap={}#l을 대신하기 위한 필드 딕셔너리
visited={}
dir = [(0,-1),(0,1),(1,0),(-1,0)]


#처음 팀에 대한 정보를 수집하기 위한 전처리 함수
def firstBfs(visited,l,node):
    global teamNo

    seq=0
    N = len(l)

    if node in visited:
        return

    team[teamNo] = {"list": []}
    team[teamNo]["count"]=1
    team[teamNo]["reverse"]=False
    q = dq()

    visited[node]=True
    teamMap[node]=(teamNo,seq)
    seq+=1
    team[teamNo]["list"].append(node)
    q.append(node)

    while q:
        dx,dy = q.popleft()
        for tx,ty in dir:
            if tx+dx>=0 and tx+dx<N and ty+dy>=0 and ty+dy<N and (tx+dx,ty+dy) not in visited and l[tx+dx][ty+dy]!=0:
                if l[dx][dy]==1 and (l[dx+tx][dy+ty]==3 or l[dx+tx][dy+ty]==4):
                    continue
                visited[(tx+dx,ty+dy)]=True
                if l[tx+dx][ty+dy]!=4:

                    teamMap[(tx+dx,ty+dy)]=(teamNo,seq)
                    seq+=1
                    team[teamNo]["count"]+=1

                team[teamNo]["list"].append((tx+dx,ty+dy))
                q.append((tx+dx,ty+dy))
    teamNo+=1



def getStartInfo(n,round): #공날라 오는 순서 처리 함수
    if (round//n)%4==0:
        return (round%n,0,0)
    elif (round//n)%4==1:
        return (n-1,round%n,1)
    elif (round//n)%4==2:
        return (n-1-round%n,n-1,2)
    elif (round//n)%4==3:
        return (0,n-1-round%n,3)

#이동을 처리하는 함수
def teamMove(teamMap,team,n):
    for no in team:
        toMove = {}
        teamList = team[no]["list"]
        isReverse = team[no]["reverse"]
        totalCount = team[no]["count"]

        for x,y in teamList:
            if (x,y) in teamMap:
                mySeq = teamMap[(x,y)][1]
                for dx,dy in dir:
                    if x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<n and (x+dx,y+dy) in teamList:
                        if isReverse==False and mySeq==0:
                            if (x+dx,y+dy) not in teamMap:
                                toMove[(x+dx,y+dy)]=teamMap[(x,y)]
                            elif (x+dx,y+dy) in teamMap and teamMap[(x+dx,y+dy)][1]==totalCount-1:
                                toMove[(x + dx, y + dy)] = teamMap[(x, y)]

                        elif isReverse==False and mySeq>0 and mySeq+1<totalCount and (x+dx,y+dy) in teamMap and teamMap[(x+dx,y+dy)][1]<mySeq:
                            toMove[(x+dx,y+dy)]=teamMap[(x,y)]

                        elif isReverse==False and mySeq+1==totalCount and (x+dx,y+dy) in teamMap and teamMap[(x+dx,y+dy)][1]!=0:
                            toMove[(x + dx, y + dy)] = teamMap[(x, y)]

                        elif isReverse==True and mySeq + 1 == totalCount and (x+dx,y+dy) not in teamMap:
                            toMove[(x+dx,y+dy)]=teamMap[(x,y)]

                        elif isReverse==True and mySeq + 1 == totalCount and (x+dx,y+dy) in teamMap and teamMap[(x+dx,y+dy)][1]==0:
                            toMove[(x + dx, y + dy)] = teamMap[(x, y)]

                        elif isReverse==True and mySeq != 0 and mySeq+1 != totalCount and (x+dx,y+dy) in teamMap and teamMap[(x+dx,y+dy)][1]>mySeq:
                            toMove[(x+dx,y+dy)]=teamMap[(x,y)]
                        elif isReverse==True and mySeq ==0 and (x+dx,y+dy) in teamMap and teamMap[(x+dx,y+dy)][1]!=totalCount-1:
                            toMove[(x + dx, y + dy)] = teamMap[(x, y)]
        for x in teamList:
            if x in teamMap:
                del teamMap[x]
        for x in toMove:
            teamMap[x]=toMove[x]







#bfs별로 좌표로 팀원들 기록해놓고, 팀별로 머리 꼬리 위치 기록해놓고 라운드 돌리기
visited={}
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            firstBfs(visited,l,(i,j))

round =0
whileDir={0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
while True:
    round+=1
    teamMove(teamMap,team,n)

    sx,sy,sdir = getStartInfo(n,round-1) # 0 오른쪽 1 위쪽 2 왼쪽 3아래쪽

    #이제 부터 l은 쓸모가 없다
    dx,dy = whileDir[sdir]
    while sx>=0 and sx<n and sy>=0 and sy<n:
        if (sx,sy) in teamMap:
            number,seqN = teamMap[(sx,sy)]

            isReverse = team[number]["reverse"]

            if not isReverse:
                score += (seqN+1)*(seqN+1)

                team[number]["reverse"]=True
            else:
                score += (team[number]["count"]-seqN)*(team[number]["count"]-seqN)

                team[number]["reverse"] = False
            break
        else:
            sx=sx+dx
            sy=sy+dy
    if round==k:
        break
print(score)