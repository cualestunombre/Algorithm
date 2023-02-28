import copy
from collections import deque
import sys
limit_number = 200000
sys.setrecursionlimit(limit_number)
def dp(who,bool):
    if (who,bool) in cache:
        return cache[(who,bool)]
    if bool==False:
        sum=0
        if who in bossMap:
            for i in bossMap[who]:
                a,b=(dp(i,True),dp(i,False))
                temp = [a,b]
                temp.sort(reverse=True)
                if a==temp[0]:
                    if (who,False) in path:
                        path[(who,False)].append((i,True))
                    else:
                        path[(who,False)]=[(i,True)]
                else:
                    if (who,False) in path:
                        path[(who,False)].append((i,False))
                    else:
                        path[(who,False)]=[(i,False)]
                sum += temp[0]
        else:
            cache[(who,bool)]=0
            return 0
        cache[(who,bool)]= sum
        return cache[(who,bool)]
    else:
        sum=0
        if who in bossMap:
            for i in bossMap[who]:

                a = dp(i,False)
                sum+=a
                if (who,True) in path:
                    path[(who, True)].append((i, False))
                else:
                    path[(who, True)] = [(i, False)]
        else:
            cache[(who,bool)]=point[who]
            return point[who]
        cache[(who,bool)]=sum+point[who]
        return cache[(who,bool)]

n=int(input())
point = [0] +list(map(int,input().split()))
boss= [0,0]+ list(map(int,input().split()))
bossMap={}
for i in range(2,len(boss)):
    #i가 부하 boss[i]가 상관
    if boss[i] not in bossMap:
        bossMap[boss[i]]=[i]
    else:
        bossMap[boss[i]].append(i)
path={}
cache={}
score1=dp(1,True)
cache={}
path2 = copy.deepcopy(path)
path={}
score2=dp(1,False)






print(str(score1)+" "+str(score2))


answer1=[1]
q=deque([(1,True)])
while q:
    x,y = q.popleft()
    if (x,y) in path2:
        for u,t in path2[(x,y)]:
            if t:
                answer1.append(u)
            q.append((u,t))
answer2=[]
q=deque([(1,False)])
while q:
    x,y = q.popleft()
    if (x,y) in path:
        for u,t in path[(x,y)]:
            if t:
                answer2.append(u)
            q.append((u,t))
answer1.sort()
answer2.sort()
for i in answer1:
    print(i,end=" ")
print(-1)
for i in answer2:
    print(i,end=" ")
print(-1)










