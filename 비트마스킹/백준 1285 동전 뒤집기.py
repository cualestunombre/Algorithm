n = int(input())
l,generated = [],[]
ret = [list(input()) for i in range(n)]
comp = int(''.join(["1" for i in range(n)]),2)

minimum = 10*100
for i in ret:
    s = []
    for j in i:
        if j == "H":
            s.append("1")
        else:
            s.append("0")
    s = ''.join(s)
    l.append(int(s,2))

for i in range(2**n):
    memo = []
    count = 0
    s = format(i,f'0{n}b')
    for j in range(n):
        if s[j] == '1':
            memo.append(j)
            l[j] = l[j] ^ comp
    strings = []
    for j in l:
        strings.append(format(j,f'0{n}b'))
    for j in range(n):
        ret = 0
        for k in range(n):
            if strings[k][j] == '1':
                ret += 1
        count += min(ret,n-ret)
    minimum = min(count,minimum)
    for j in memo:
        l[j] = comp ^ l[j]
print(minimum)

