n,m = map(int,input().split())
l=[int(input()) for i in range(n)]
start=0
end=1000000000000000000
ans=0
while start<=end:
    mid = (start+end)//2
    cnt = 0
    for i in range(n):
        cnt+=mid//l[i]

    if cnt>=m:
        ans=mid
        end=mid-1
    else:
        start=mid+1
print(ans)


