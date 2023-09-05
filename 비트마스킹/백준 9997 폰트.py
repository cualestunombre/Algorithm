global n
n = int(input())
l = [input() for i in range(n)]
alphabet = {}

for i in range(26):
    alphabet[chr(i+97)] = i
decimal = []

for i,elements in enumerate(l):
    ret = 0
    for element in elements:
        ret = ret | 2**alphabet[element]
    decimal.append(ret)



def brute(comp,step):
    global n
    ret = comp | decimal[step] #현재에 쓴 것

    if ret == 2**26-1:
        return 1 if step == n-1 else 2**(n-1-step) + brute(comp,step+1)
    elif step == n - 1:
        return 0

    return brute(ret,step + 1) + brute(comp,step+1)

print(brute(0,0)) #