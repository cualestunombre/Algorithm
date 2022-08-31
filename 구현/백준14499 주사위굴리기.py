n,m,x,y,k = map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
orders = list(map(int,input().split()))
data={1:0,2:0,3:0,4:0,5:0,6:0}
pos={1:1,2:2,3:3,4:4,5:5,6:6}
dir={1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}
curx=x
cury=y
cur=1
ans=[]
def turn(pos,num):
    arr=[pos[i] for i in range(1,7)]
    if num==1:
        pos[1]=arr[2]
        pos[3]=arr[5]
        pos[4]=arr[0]
        pos[6]=arr[3]
    if num==2:
        pos[1]=arr[3]
        pos[3]=arr[0]
        pos[4]=arr[5]
        pos[6]=arr[2]
    if num==3:
        pos[1]=arr[1]
        pos[5]=arr[0]
        pos[6]=arr[4]
        pos[2]=arr[5]
    if num==4:
        pos[1]=arr[4]
        pos[5]=arr[5]
        pos[2]=arr[0]
        pos[6]=arr[1]

for i in orders:
    sx,sy=dir[i]
    if curx+sx>=0 and curx+sx<=n-1 and cury+sy>=0 and cury+sy<=m-1:
        curx+=sx
        cury+=sy
        turn(pos,i)
        cur=pos[1]
        if l[curx][cury]==0:
            l[curx][cury]=data[cur]
        else:
            data[cur]=l[curx][cury]
            l[curx][cury]=0
        ans.append(data[7-cur])
for i in ans:
    print(i)




