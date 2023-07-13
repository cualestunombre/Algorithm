import sys
sys.setrecursionlimit(10000)
n = int(input())
cand = [0]

def backTrack(cur):
    last = int(cur[-1])
    for i in range(last-1,-1,-1):
        cand.append(int(''.join(cur)+str(i)))
        cur.append(str(i))
        backTrack(cur)
        cur.pop()
    return



for i in range(1,10):
    cand.append(i)
    backTrack([str(i)])

cand.sort()
if len(cand)-1 < n:
    print(-1)
else:
    print(cand[n])