n = int(input())
weights = list(map(int,input().split()))
marble_count = int(input())
marbles = list(map(int,input().split()))
cache = {}

def dp(step,left,right,result):
    global n
    if abs(left-right) not in result:
        result.add(abs(left-right))

    if step == n:
        return

    if (step,abs(left-right)) not in cache:
        dp(step+1,left+weights[step],right,result)
        dp(step + 1, left, right+ weights[step], result)
        dp(step + 1, left, right, result)
        cache[(step,abs(left-right))] = True
result = set()
dp(0,0,0,result)
for marble in marbles:
    if marble in result:
        print("Y",end=" ")
    else:
        print("N",end=" ")
