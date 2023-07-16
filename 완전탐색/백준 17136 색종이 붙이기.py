n = int(input())
l = list(map(int,input().split()))
plusOrZero = [i for i in l if i>=0 ]
minus = [i for i in l if i<0]

plusOrZero.sort()
minus.sort()
print(plusOrZero)
print(minus)