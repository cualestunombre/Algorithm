import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
cache={0:['0'],1:['1'],2:['1','0'],3:['1','0','0'],4:['1','0','1']}
n=int(input())
an=[0,1]
sn=[0]
cur=1
for i in range(99):
    an.append(an[cur]+an[cur-1])
    cur+=1
cur=1
for i in range(99):
    sn.append(sn[cur-1]+an[cur])
    cur+=1

def dp(n):
    if n in cache:
        return cache[n]
    else:
        length = 0
        for i in range(len(sn)):
            if n <= sn[i]:
                length = i
                break
        count=an[length]
        prevCount=an[length-1]
        temp = dp(n-count-prevCount)
        aux = ['1','0']
        for i in range(length-2-len(temp)):
            aux.append('0')
        cache[n] = aux+temp
        return cache[n]
print("".join(dp(n)))


