n=int(input())
l=list(map(int,input().split()))
dic={}
for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
ll = []
for i in l: #숫자 회수
    ll.append((i,dic[i]))
stack=[0]
ans=[-1 for i in range(n)]
for i in range(1,len(ll)):
    while stack and ll[i][1]>ll[stack[-1]][1]:
        ans[stack.pop()]=ll[i][0]
    stack.append(i)
print(*ans)