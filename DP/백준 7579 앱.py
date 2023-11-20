global n,m
n,m = map(int,input().split()) # 앱 개수, 필요 메모리
memories = list(map(int,input().split()))
cost = list(map(int,input().split()))

cache = [[0 for _ in range(sum(cost) + 1)] for __ in range(n+1)]
for _ in range(n):
    cache[_+1][cost[_]] = memories[_]
# 사용 인덱스, 비용
for _ in range(1,n+1):
    for __ in range(sum(cost) + 1):
        if __ - cost[_-1] >= 0:
            # 사용 인덱스, 비용 중에서 메모리가 최대인 것을 고르겠다
            cache[_][__] = max(cache[_-1][__],cache[_-1][__ - cost[_-1]] + memories[_-1])
        else:
            cache[_][__] = cache[_-1][__]

for i in range(sum(cost)+1):
    if cache[n][i] >= m:
        print(i)
        break


