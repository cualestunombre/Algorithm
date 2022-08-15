n,m = map(int,input().split())
l=list(map(int,input().split()))

if n<m:
    print(n)
else:
    start=0
    time=0
    end=60000000000
    while start<=end:
        mid = (start+end)//2
        cnt=m
        for i in range(m):
            cnt+=mid//l[i]
        if cnt>=n:
            time=mid
            end=mid-1
        else:
            start=mid+1
    cnt=m
    for i in range(m):
        cnt+=(time-1)//l[i]
    for i in range(m):
        if time%l[i]==0:
            cnt+=1
            if n==cnt:
                print(i+1)
                break

# comment : 이분 탐색에서, 무엇을 기준으로 이분탐색할 것 인가를 생각해보게 하는 문제