r,c,k = map(int,input().split())
l=[list(map(int,input().split())) for i in range(3)]
time=0
while True:
    if (r-1>=0 and r-1<=len(l)-1 and c-1>=0 and c-1<=len(l[0])-1):
       if l[r-1][c-1]==k:
           break

    time+=1
    row= len(l)
    col= len(l[0])
    if row>=col:
        for i in range(row):
            dic={}
            for j in l[i]:
                if j==0:
                    continue
                if j not in dic:
                    dic[j]=1
                else:
                    dic[j]+=1
            temp=[]
            for j in dic:
                temp.append((j,dic[j]))
            temp.sort(key=lambda x:(x[1],x[0]))
            temp2=[]
            for x,y in temp:
                temp2.append(x)
                temp2.append(y)
            while len(temp2)>=101:
                temp2.pop()
            del l[i]
            l.insert(i,temp2)
        biggest=0
        for i in l:
            if len(i)>biggest:
                biggest = len(i)
        for i in l:
            if len(i)<biggest:
                for j in range(biggest-len(i)):
                    i.append(0)
    else:
        colL=[[]for i in range(col)]
        for i in range(row):
            for j in range(col):
                colL[j].append(l[i][j])
        for i in range(col):
            dic={}
            for j in colL[i]:
                if j==0:
                    continue
                if j not in dic:
                    dic[j]=1
                else:
                    dic[j]+=1
            temp=[]
            for j in dic:
                temp.append((j,dic[j]))
            temp.sort(key=lambda x:(x[1],x[0]))
            temp2=[]
            for x,y in temp:
                temp2.append(x)
                temp2.append(y)
            while len(temp2)>=101:
                temp2.pop()
            del colL[i]
            colL.insert(i,temp2)
        biggest=0
        for i in colL:
            if len(i)>biggest:
                biggest = len(i)
        for i in colL:
            if len(i)<biggest:
                for j in range(biggest-len(i)):
                    i.append(0)
        l=[[]for i in range(len(colL[0]))]
        for i in range(len(colL)):
            for j in range(len(colL[0])):
                l[j].append(colL[i][j])

    if time>100:
        break

if time>100:
    print(-1)
else:
    print(time)






