global n,l,r,x
n,l,r,x = map(int,input().split())
# n개 문제, l보다 크거나 같고, r보다 작거나 같다, 가장 쉬운문제와 작은 문제의 난이도 차는 X보다 크거나 같아야 한다
cand = list(map(int,input().split()))
cache = [-1 for i in range(2**n)]

def dp(c,step):
    global n,l,r,x
    if cache[c] != -1:
        return cache[c]
    if step == n-1:
        bs = format(c,f'0{n}b')
        hardest = 0
        easiest = 10**20
        ret = 0
        for i in range(len(bs)-1,-1,-1):
            if bs[i] == "1":
                ret += cand[i]
                hardest = max(hardest,cand[i])
                easiest = min(easiest,cand[i])
        if ret>=l and ret<=r and hardest - easiest>=x:
            cache[c] = 1
            return 1
        cache[c] = 0
        return 0

    bs = format(c, f'0{n}b')
    ret = 0
    for i in range(len(bs) - 1, -1, -1):
        if bs[i] == "1":
            ret += cand[i]

    if ret > r:
        cache[c] = 0
        return 0
    cache[c] = dp(c,step+1) + dp(c+2**(step+1),step+1)

    return cache[c]










print(dp(1,0)+dp(0,0))
