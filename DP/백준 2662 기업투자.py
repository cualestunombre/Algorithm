global n,m
n,m = map(int,input().split()) # 총 투자 금액, 투자 가능 기업
l = [list(map(int,input().split())) for i in range(n)]
cache = {}

def dp(step,left):
    global n,m
    if (step,left) in cache:
        return cache[(step,left)][0]
    if step == m:
        return 0

    profit,value = dp(step+1,left),0

    for i in range(n):
        if i+1 <= left:
            ret = dp(step + 1, left - i - 1) + l[i][step+1]
            if ret > profit:
                profit = ret
                value = i + 1

    cache[(step,left)] = (profit,value)
    return profit



profit,value = dp(1,n),0
for i in range(n):
    ret = dp(1,n-i-1) + l[i][1]
    if ret > profit:
        profit = ret
        value = i + 1
print(profit)
print(value,end=" ")
cur = n - value
for i in range(1,m):
    p,v = cache[(i,cur)]
    cur -= v
    print(v,end=" ")


