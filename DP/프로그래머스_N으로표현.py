def solution(number,N):
    dp=[]
    for i in range(1,9):
        bucket = set()
        bucket.add(int(str(number)*i))
        for j in range(0,i-1):
            for k in dp[j]:
                for l in dp[-j-1]:
                    if k+l !=0:
                        bucket.add(k+l)
                    if abs(k-l)!=0:
                        bucket.add(k-l)
                        bucket.add(l-k)
                    bucket.add(l * k)
                    if (l//k!=0):
                        bucket.add(l//k)
                    if (k//l!=0):
                        bucket.add(k//l)
        if N in bucket:
            return i
        dp.append(bucket)
    return -1
