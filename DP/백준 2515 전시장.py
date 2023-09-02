import sys

m, n = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(m)]  # 높이, 돈
l.sort(key=lambda x: -x[0])
l.append((0, 0))
end = len(l)
cache = [[-1 for _ in range(2)] for _ in range(len(l) + 1)]

def binarySearch(s, e, h, n):  # 시작, 종료, 높이, 허용 높이차
    t = e

    while s <= e:
        mid = (s + e) // 2
        mh = l[mid][0]
        if h - mh >= n:
            e = mid - 1
            t = mid
        else:
            s = mid + 1

    return t

for stage in range(end - 1, -1, -1):
    for flag in range(2):
        if cache[stage][flag] == -1:
            if stage == end - 1:
                cache[stage][flag] = 0
            elif flag == 0:
                cache[stage][flag] = max(cache[stage + 1][1], cache[stage + 1][0])
            else:
                if l[stage][0] - l[stage + 1][0] >= n:
                    cache[stage][flag] = max(cache[stage + 1][0], cache[stage + 1][1]) + l[stage][1]
                else:
                    targetIndex = binarySearch(stage + 2, len(l) - 1, l[stage][0], n)
                    cache[stage][flag] = max(cache[targetIndex][0], cache[targetIndex][1]) + l[stage][1]

print(max(cache[0][0], cache[0][1]))
