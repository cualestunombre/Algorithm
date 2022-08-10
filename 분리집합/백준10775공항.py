
parent={}
def find(x):
    if parent[x]!=x:
        return find(parent[x])
    else:
        return x
def union(x):
    u = find(x)
    v= find(x-1)
    parent[u]=v
q = []
g = int(input())
p = int(input())
l = [int(input()) for i in range(p)]
count=0
for i in range(0,g+1):
    parent[i]=i
for i in l:
    x= find(i)
    if x==0:
        break
    union(x)
    count+=1
print(count)

