import sys
input = sys.stdin.readline
n,c= map(int,input().split())
m=int(input())
l=[tuple(map(int,input().split()))for i in range(m)]
l.sort(key=lambda x:x[1]) 
count=[0 for i in range(n+1)]
score=0
for a_,b_,c_ in l:
    possi=100000000000000
    for j in range(a_,b_):
        possi=min(possi,c-count[j])
    target = min(possi,c_)
    for j in range(a_,b_):
        count[j]+=target
    score+=target
print(score)