#수명다한 제초제 제거
def handlePesticide(l,pesticide):
    change={}
    for x,y in pesticide:
        pesticide[(x,y)]-=1
        if pesticide[(x,y)]==-1:
            change[(x,y)]=True
            l[x][y]=0
    for x,y in change:
        del pesticide[(x,y)]


#나무번식
def treeGrow(l):
    n=len(l)
    for row in range(n):
        for col in range(n):
            if l[row][col]>=1:
                count=0
                for dx,dy in dir:
                    if row+dx>=0 and row+dx<n and col+dy>=0 and col+dy<n and l[row+dx][col+dy]>=1:
                        count+=1
                l[row][col]+=count


#나무전파
def treePropagate(l):

    change={}
    n=len(l)

    for row in range(n):
        for col in range(n):
            amount = l[row][col]
            if amount<1:
                continue
            can_propagate=0
            pos = {}
            for dx,dy in dir:
                if row+dx>=0 and row+dx<n and col+dy>=0 and col+dy<n and l[row+dx][col+dy]==0:
                    can_propagate+=1
                    pos[(row+dx,col+dy)]=True
            if can_propagate>0:
                amount = amount//can_propagate
                for x,y in pos:
                    if (x,y) in change:
                        change[(x,y)]+=amount
                    else:
                        change[(x,y)]=amount
    #실제 업데이트
    for x,y in change:
        l[x][y]+=change[(x,y)]

#제초제 살포
def spreadPesticide(l,pesticide):
    global k,c
    _max=0
    count = 0
    n = len(l)
    array=[]

    for row in range(n):
        for col in range(n):
            if l[row][col]>=1:
                # 어디가 가장 효과적인지 계산
                ret = effect(row,col,l)
                array.append((row,col,ret))
            elif l[row][col]==0 or l[row][col]==-2:
                array.append((row,col,0))

    array.sort(key=lambda x:(-x[2],x[0],x[1]))

    x,y,dummy =array[0]


    #살포한 칸에 대한 처리
    if l[x][y]>0:
         count += l[x][y]
    l[x][y]=-2
    pesticide[(x,y)]=c

    if count==0:
        return 0

    for dx,dy in diagonal:
        for r in range(1,k+1):
            nx,ny = dx*r, dy*r
            if x+nx>=0 and x+nx<n and y+ny>=0 and y+ny<n:
                if l[x+nx][y+ny]==0:
                    l[x+nx][y+ny]=-2
                    pesticide[(x+nx,y+ny)]=c
                    break
                elif l[x+nx][y+ny]==-2:
                    pesticide[(x+nx,y+ny)]=c
                    break
                elif l[x+nx][y+ny]==-1:
                    break
                count+=l[x+nx][y+ny]
                l[x+nx][y+ny]=-2
                pesticide[(x+nx,y+ny)]=c
            else:
                break
    return count

def effect(row,col,l):
    global k
    n=len(l)
    cnt=0
    cnt+=l[row][col]
    for dx,dy in diagonal:
        for r in range(1,k+1):
            nx,ny = dx*r, dy*r
            if row+nx>=0 and row+nx<n and col+ny>=0 and col+ny<n:
                if l[row+nx][col+ny]==0:
                    break
                elif l[row+nx][col+ny]==-2:
                    break
                elif l[row+nx][col+ny]==-1:
                    break
                cnt+=l[row+nx][col+ny]
            else:
                break
    return cnt
def probe(l):
    for i in l:
        for j in i:
            print(j,end=" ")
        print("")
    print("")



#빈칸 0 벽 -1 제초제 -2
global k,c
n,m,k,c = map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
dir=[(0,-1),(0,1),(1,0),(-1,0)]
diagonal=[(1,1),(1,-1),(-1,1),(-1,-1)]
#제초제 위치와 수명
pesticide={}
score=0
round=0
while True:
    round+=1

    #수명 다한 제초제 제거 - 0 단계
    handlePesticide(l,pesticide)


    #나무 성장 - 1 단계
    treeGrow(l)


    #나무 번식 - 2 단계
    treePropagate(l)




    #제초체 살포 - 3 단계
    score += spreadPesticide(l,pesticide)




    if round==m:
        break

print(score)

