global n
n = int(input())
cache = [[[-1 for k in range(1024)] for j in range(n)] for i in range(10)]

#현재 숫자, 현재 단계, 현재 필드

def dp(number,step,field): # 10가지 * 100가지 * field 1024가지
    global n
    if cache[number][step][field] != -1:
        return cache[number][step][field]

    if step == n-1:
        if field == 1023:
            cache[number][step][field] = 1
            return 1
        else:
            cache[number][step][field] = 0
            return 0


    ret = 0
    if number - 1 >= 0:
        arr = list(format(field,f'0{10}b'))
        arr[9-number+1] = '1'
        ret += dp(number-1,step+1,int(''.join(arr),2))

    if number + 1 <= 9:
        arr = list(format(field,f'0{10}b'))
        arr[9-number-1] = '1'
        ret += dp(number+1,step+1,int(''.join(arr),2))


    cache[number][step][field] = ret
    return  cache[number][step][field]





answer = 0
for i in range(1,10):
    answer += dp(i,0,2**i)

print(answer% 1000000000)



