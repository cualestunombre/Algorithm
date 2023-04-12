import sys
def input():
    return sys.stdin.readline().rstrip()
def count_group(val):
    k = 0
    temp = 0
    for ind in range(N):
        temp += arr[ind]
        if temp >= val:
            k += 1
            temp = 0
    return k


N, K = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = sum(arr) + 1

while left+1 < right:
    mid = (left + right) // 2
    K_mid = count_group(mid)
    if K_mid >= K:
        left = mid
    else:
        right = mid
print(left)