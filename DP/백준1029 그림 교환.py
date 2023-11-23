n = int(input())
l = [[int(__) for __ in list(input()) ] for _ in range(n)]
cache = [[[-1 for ___ in range(10)] for __ in range(n+1)] for _ in range(2**n)]

def dp(field,owner,price):
    global n
    if cache[field][owner][price] != -1:
        return cache[field][owner][price]

    ret = 0
    string_field = list(format(field,f'0{n}b'))
    for new_owner in range(n):
        if string_field[new_owner] == '0' and l[owner][new_owner] >= price:
            string_field[new_owner] = '1'
            ret = max(ret, dp(int(''.join(string_field),2),new_owner,l[owner][new_owner]))
            string_field[new_owner] = '0'

    cache[field][owner][price] = ret + 1
    return ret + 1


print(dp(2**(n-1),0,0))
