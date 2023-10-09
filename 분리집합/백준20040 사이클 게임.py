import sys
sys.setrecursionlimit(200000)
n,m= map(int,input().split())
l = [tuple(map(int,input().split())) for i in range(m)]
parent = {}

def findParent(i):
   if parent[i] == i:
       return i
   else:
       parent[i] = findParent(parent[i])
       return parent[i]

def union(u,v):
    parentU,parentV = findParent(u),findParent(v)
    parent[parentU] = parentV

for i in range(n):
    parent[i] = i

turn = 1
flag = False
for x,y in l:
    if findParent(x) == findParent(y):
        flag = True
        break
    else:
        union(x,y)
    turn+=1

if flag:
    print(turn)
else:
    print(0)




