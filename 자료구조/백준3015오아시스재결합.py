n=int(input())
l=[int(input()) for _ in range(n)]
s=[[1,l[-1]]] #횟수, 숫자
num=0
for i in range(n-2,-1,-1):
    t=[]
    if l[i]<l[i+1]:
        num+=1
    else:
        while s:
            if l[i]>s[-1][1]:
                num+=s.pop()[0]
            elif l[i]==s[-1][1]:
                t.append((s[-1][0]))
                num+=s.pop()[0]
            else:
                num+=1
                break
    if t:
        s.append([t[0]+1,l[i]])
    else:
        s.append([1,l[i]])
print(num)
