n=int(input())
l=list(map(int,input().split()))
a=[-1]*n
s=[0] #스택에 들어가는 수를 인덱스화 하였음
for i in range(1,n):
    while s and l[s[-1]]<l[i]:
        a[s.pop()]=l[i]
    s.append(i)
print(*a)
