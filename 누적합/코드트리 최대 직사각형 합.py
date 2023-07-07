global n,maxValue
maxValue = -1000000000000000000000000
n = int(input())
cache = {}
l = [[0 for i in range(n+1)]]+[[0]+list(map(int,input().split())) for i in range(n)]
temp = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        l[i][j] = l[i][j] + l[i][j-1]
for i in range(n+1):
    for j in range(n+1):
        temp[i][j] = l[i][j] + temp[i-1][j]

def func(i,j):
    global n,maxValue
    curMax = 0
    for k in range(1,n+1):
        curMax += temp[i][k] - temp[j][k] - temp[i][k-1] + temp[j][k-1]
        if curMax > maxValue:
            maxValue = curMax
        if curMax<0:
            curMax = 0


for i in range(1,n+1):
    for j in range(0,i):
        value = func(i,j)
print(maxValue)