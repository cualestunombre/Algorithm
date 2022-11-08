n=int(input())
l=list(map(int,input().split()))

lis=[-100000000000000000]

for i in l:
    if i>lis[-1]:
        lis.append(i)
    else:
        start=1
        end=len(lis)-1
        while start<end:
            mid=(start+end)//2
            if i<lis[mid]:
                end=mid
            elif i>lis[mid]:
                start=mid+1
            elif i==lis[mid]:
                start=end=mid
        lis[end]=i

print(len(lis)-1)