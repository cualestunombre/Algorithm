n=int(input())
l=[input()for _ in range(n)]
d={}
for i in l:
 s=len(i)
 for j in range(s):
  d[i[j]]=d.get(i[j],0)+10**(s-j-1)
e=sorted(d.values(),reverse=True)
print(sum((9-i)*e[i]for i in range(len(e))))
